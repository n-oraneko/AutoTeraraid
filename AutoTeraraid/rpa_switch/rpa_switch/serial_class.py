import yaml
import time
import serial

class serial_class:
    def __init__(self, port,baudrate,tap_sec):
        self.connection_fat32(port,baudrate)
        self.tap_sec = tap_sec
        self.release = 100
        self.button_dict={
            'Y' :1 ,
            'B' :2,
            'A' :3 ,
            'X' :4 ,
            'L' :5 ,
            'R' :6 ,
            'ZL' :7 ,
            'ZR' :8 ,
            'MINUS' :9, 
            'PLUS' :10 ,
            'LCLICK' :11, 
            'RCLICK' :12 ,
            'HOME' :13 ,
            'CAPTURE' :14, 

            'UP' :15 ,
            'UP_RIGHT' :16, 
            'RIGHT' :17 ,
            'DOWN_RIGHT' :18, 
            'DOWN' :19 ,
            'DOWN_LEFT' :20, 
            'LEFT' :21 ,
            'UP_LEFT' :22 , 
            'NEUTRAL' :23, 

            'left' :200,
            'neutralLeft' :201,
            'right' :202,
            'neutralRight' :203
        }
    def __del__(self):
        self.ser.close()

    def connection_fat32(self,port,baudrate):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.setDTR(False) 
        self.ser.open()

        
    def tap(self,buttons):
        #押す
        for btn in buttons:
            print('button press:',btn)
            self.ser.write(bytes([self.button_dict[btn]]))
        time.sleep(self.tap_sec)
        #離す
        for btn in buttons:
            self.ser.write(bytes([self.button_dict[btn]+self.release]))

    def press(self,buttons):
        #押す
        for btn in buttons:
            self.ser.write(bytes([self.button_dict[btn]]))

    def release_button(self,buttons):
        #離す
        for btn in buttons:
            self.ser.write(bytes([self.button_dict[btn]+self.release]))

    def stick(self,stick,x,y,stick_time):
        self.ser.write(bytes([self.button_dict[stick]]))
        self.ser.write(bytes(x))
        self.ser.write(bytes(y))
        time.sleep(stick_time)
        self.ser.write(bytes([self.button_dict[stick]+1]))
