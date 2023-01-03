import sys
import os
import cv2
import pyocr
import numpy as np
from PIL import Image
import sys
import time

class capture_class:
    def __init__(self, num,quality,ocr_tool):
        self.connection_display(num,quality)
        self.connection_ocr(ocr_tool)
    def __del__(self):
        self.capture.release()
        cv2.destroyAllWindows()

    def connection_ocr(self,ocr_tool):
        # 1.インストール済みのTesseractのパスを通す
        path_tesseract = ocr_tool
        if path_tesseract not in os.environ["PATH"].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + path_tesseract
        self.ocr_tools = pyocr.get_available_tools()
        if len(self.ocr_tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        self.tool = self.ocr_tools[0]

    def connection_display(self,num,quality):
        self.capture = cv2.VideoCapture(num)
        print(self.capture.isOpened())
        if not self.capture.isOpened():
            print("No Capture board found")
            sys.exit(1)
        self.origin_width = 1920
        self.origin_heigt = 1080
        self.capture.set(3, self.origin_width//quality)
        self.capture.set(4, self.origin_heigt//quality)
        
    def read_now(self,frame_num,sleep_time):
        #前のフレームを破棄
        for i in range(frame_num):
            time.sleep(sleep_time)
            self.ret, self.frame = self.capture.read()

    def trimming(self,y_start,y_end,x_start,x_end):
        y_start = int(y_start * len(self.frame)/self.origin_heigt)
        y_end = int(y_end *  len(self.frame)/self.origin_heigt)
        x_start = int(x_start * len(self.frame[0])/ self.origin_width  )
        x_end = int(x_end *  len(self.frame[0])/ self.origin_width)
        self.trim_img = self.frame[y_start:y_end,x_start:x_end]

    def check_ocr(self,message):
        ##とりあえず二値化するか
        ##threshold
        #im_gray = cv2.cvtColor(self.trim_img, cv2.COLOR_BGR2GRAY)
        #im_blur = cv2.GaussianBlur(im_gray, (5, 5), 0)
        #bin_img = cv2.adaptiveThreshold(im_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #cv2.imwrite("target.png",bin_img)
        cv2.imwrite("target.png",self.trim_img)
        res_string = self.tool.image_to_string(Image.open("target.png") , lang="jpn")
        if not res_string == '':
            print("text:",res_string.replace('\r\n',' '))
        if message in res_string:
            return True
        else :return False
        

    def check_color(self,color,reliability,frame):
        #average_color_row = np.average(frame, axis=0)
        #average_color = np.average(average_color_row, axis=0)
        average_color = self.calc_color(frame)
        if (average_color[0]-reliability < color[0] and 
            color[0] < average_color[0]+reliability and
            average_color[1]-reliability < color[1] and 
            color[1] < average_color[1]+reliability and
            average_color[2]-reliability < color[2] and 
            color[2] < average_color[2]+reliability ):
                return True
        return False

    def check_color_trim(self,color,reliability):
        return self.check_color(color,reliability,self.trim_img)

    def calc_color(self,frame):
        average_color_row = np.average(frame, axis=0)
        return np.average(average_color_row, axis=0)