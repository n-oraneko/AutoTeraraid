import sys
import yaml
import time
import status_class

def thread_control():
    global status
    #メイン関数
    with open(sys.argv[1] ,'r', encoding="utf-8") as file:
        rpa_yml = yaml.safe_load(file)
    print("control func start")
    status = status_class.status_class(rpa_yml)
    loop_cnt = rpa_yml["loop"]
    try:
        if loop_cnt == -1:
            while True:
                status.status_control()
        else :
            for i in range(loop_cnt):
                status.status_control()
        all_close()
    except Exception as e:
        print(e,':',str(e))
        all_close()

def all_close():
    global status
    status.all_close()




def frame_control(sleep_time,status):
    status.status_control()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("rpa設定ファイルを引数で指定してください")
    thread_control()


