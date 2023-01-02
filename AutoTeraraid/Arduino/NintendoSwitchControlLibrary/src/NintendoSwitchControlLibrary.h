/*
Copyright (c) 2021 lefmarna
released under the MIT license
https://opensource.org/licenses/mit-license.php
rewrite by noraneko
*/

#pragma once

#include "./SwitchControlLibrary/SwitchControlLibrary.h"

// 各種ボタンの設定(ABXYだけでなく、HOMEやCAPTUREまで幅広く対応)
void pushButton(uint16_t button);
void pushUpButton(uint16_t button);
// 十字キーの設定
void pushHat(uint8_t hat);
void pushUpHat(uint8_t hat);
// スティックの設定
void tiltLeftStick(uint8_t lx, uint8_t ly);
void neutralLeftStick(void);
void tiltRightStick(uint8_t rx, uint8_t ry);
void neutralRightStick(void);