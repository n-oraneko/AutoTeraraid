from multiprocessing import Event
import yaml
from enum import Enum
import capture_class
import serial_class
import time

# 状態列挙型の定義
class STATUS(Enum):
    START = 1
    SCENARIO = 2
    EVENT = 3
    END = 4
    ERROR = 5

class status_class:

    def __init__(self,input_setting):
        print("初期設定開始")
        self.error_count=0
        self.error_color = [0,0,0]
        self.setting = input_setting
        self.capture_cls = capture_class.capture_class(self.setting["capture_borad"],self.setting["capture_image_quality"],self.setting["oct_tool"])
        self.serial_cls = serial_class.serial_class(self.setting["serial_port"],self.setting["baudrate"],self.setting["tap_sec"])
        self.past_event_id = -1 #ひとつ前のイベント　同一イベントを連続しないように

    def all_close(self):
        del self.capture_cls
        del self.serial_cls

        
    def status_control(self):
        #status 
        self.status = STATUS.START
        self.scene_num = 0
        self.event_scene_num = 0
        self.error_scene_num = 0 
        sleep_time = self.setting["step_sec"]

        while True:
            start_frame_time = time.time()
            #frame
            if self.frame_control(): #True : 一周終了
                break
            #ステップスリープ
            end_frame_time = time.time()
            slp_time = sleep_time - (end_frame_time - start_frame_time)
            #print('sleep:',slp_time)
            if slp_time> 0:
                time.sleep(slp_time)

    def frame_control(self):
        #フレーム画像取得
        self.capture_cls.read_now(self.setting["waste_frame_num"],self.setting["waste_frame_sleep"])
        if self.status == STATUS.START:
            self.start_control()
        elif self.status == STATUS.SCENARIO:
            self.scenario_control()
        elif self.status == STATUS.EVENT:
            self.event_control()
        elif self.status == STATUS.END:
            return True
        elif self.status == STATUS.ERROR:
            self.errror_control()
        return False
            
    def check_trigger(self,trigger):
        self.capture_cls.trimming(trigger["image"][0],trigger["image"][1],trigger["image"][2],trigger["image"][3])
        if trigger["type"] == "ocr":
            res = self.capture_cls.check_ocr(trigger["ocr_string"])
        elif trigger["type"] == "color":
            res = self.capture_cls.check_color_trim(trigger["color_value"],trigger["reliability"])
        return res


    def do_scene(self,scene):
        if scene["type"] == "tap":
            self.serial_cls.tap(scene["button"])
        elif scene["type"] == "press":
            self.serial_cls.press(scene["button"])
        elif scene["type"] == "release":
            self.serial_cls.release_button(scene["button"])
        elif scene["type"] == "stick":
            self.serial_cls.stick(scene["stick"],scene["x"],scene["y"],scene["time"])
        elif scene["type"] == "wait":
            print('sleep:',scene["time"])
            time.sleep(scene["time"])

    def check_event(self):
        if not 'event' in self.setting:
            return
        for eve in self.setting["event"]:
            if self.check_trigger(eve):
                if not eve["id"] == -1:
                    if self.past_event_id == eve["id"]:
                        return False
                self.past_event_id = eve["id"]
                self.event_senario = eve["scenario"]
                self.status = STATUS.EVENT
                return True
        return False

    def check_error(self):
        if not self.setting["is_error_trigger"]:
            return False
        if self.capture_cls.check_color(self.error_color,self.setting["error_trigger"]["reliability"],self.capture_cls.frame):
            self.error_count += 1
        else :
            self.error_count = 0
        if self.error_count > self.setting["error_trigger"]["count"]:
            self.status = STATUS.ERROR
            return True

        self.error_color = self.capture_cls.calc_color(self.capture_cls.frame)
        return False
        

    def errror_control(self):
        print('error:初期化します')
        scene = self.setting["error_trigger"]["scene"][self.error_scene_num]
        self.do_scene(scene)
        self.error_scene_num += 1
        if len(self.setting["error_trigger"]["scene"]) == self.error_scene_num:
            #終わる。
            self.status =STATUS.END

    def start_control(self):
        if not self.setting["is_start_trigger"]:
            self.status = STATUS.SCENARIO
            return True
        start_trigger = self.setting["start_trigger"]
        res = self.check_trigger(start_trigger)
        if res:
            self.status = STATUS.SCENARIO
            return True
        return False
            
    def event_control(self):
        print('event:',self.past_event_id,'  ,scene:',self.event_scene_num)
        scene = self.event_senario["scene"][self.event_scene_num]
        self.do_scene(scene)
        self.event_scene_num += 1
        if len(self.event_senario["scene"]) == self.event_scene_num:
            #終わる。
            self.status =STATUS.END

    def end_control(self):
        if not self.setting["is_end_trigger"]:
            return False
        end_trigger = self.setting["end_trigger"]
        res = self.check_trigger(end_trigger)
        if res:
            self.status = STATUS.END
            return True
        return False


    def scenario_control(self):
        if self.check_error():
            return False
        if self.end_control():
            return False
        if self.check_event():
            return False
        scene = self.setting["scenario"]["scene"][self.scene_num]
        self.do_scene(scene)
        self.scene_num += 1
        if len(self.setting["scenario"]["scene"]) == self.scene_num:
            #終わる。
            self.status =STATUS.END




