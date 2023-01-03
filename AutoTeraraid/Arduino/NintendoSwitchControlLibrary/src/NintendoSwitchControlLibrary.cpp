/*
Copyright (c) 2021 lefmarna
released under the MIT license
https://opensource.org/licenses/mit-license.php
rewrite by noraneko
*/

#include "./NintendoSwitchControlLibrary.h"

// ボタンを押してから離すまでの時間（ミリ秒）
const uint16_t INPUT_TIME = 100;

void pushButton(uint16_t button) {
    SwitchControlLibrary().pressButton(button);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void pushUpButton(uint16_t button) {
    SwitchControlLibrary().releaseButton(button);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void pushHat(uint8_t hat) {
    SwitchControlLibrary().pressHatButton(hat);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void pushUpHat(uint8_t hat) {
    SwitchControlLibrary().releaseHatButton(hat);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void tiltLeftStick(uint8_t lx, uint8_t ly) {
    /*
    Switchコントローラーの左スティックを指定の時間傾け続ける関数
    128を基準とし、0~255の値を指定する

    Parameters
    -------------------
        lx: 左スティックのx軸
        ly: 左スティックのy軸
        tilt_time: スティックを傾ける時間の長さ

    Options
    -------------------
          0: Stick::MIN
        128: Stick::NEUTRAL
        255: Stick::MAX
    */
    SwitchControlLibrary().moveLeftStick(lx, ly);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void neutralLeftStick(void){
    SwitchControlLibrary().moveLeftStick(Stick::NEUTRAL, Stick::NEUTRAL);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void tiltRightStick(uint8_t rx, uint8_t ry) {
    /*
    Switchコントローラーの右スティックを指定の時間傾け続ける関数
    128を基準とし、0~255の値を指定する

    Parameters
    -------------------
        rx: 右スティックのx軸
        ry: 右スティックのy軸
        tilt_time: スティックを傾ける時間の長さ

    Options
    -------------------
          0: Stick::MIN
        128: Stick::NEUTRAL
        255: Stick::MAX
    */
    SwitchControlLibrary().moveRightStick(rx, ry);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}

void neutralRightStick(void){
    SwitchControlLibrary().moveRightStick(Stick::NEUTRAL, Stick::NEUTRAL);
    SwitchControlLibrary().sendReport();
    delay(INPUT_TIME);
}