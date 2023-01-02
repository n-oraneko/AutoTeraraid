#include <NintendoSwitchControlLibrary.h>

int leftX;
int leftY;
int rightX;
int rightY;

void setup() {
    //pushButton(Button::HOME, 500, 4);
  for (int i = 0; i < 3; ++i) {
    pushButton(Button::HOME);
    pushUpButton(Button::HOME);
    delay(500);
  }
  Serial1.begin(115200);
}

void setControllerStates(int data) {
  if(data == 1) {pushButton(Button::Y);}
  if(data == 101) {pushUpButton(Button::Y);}
  if(data == 2) {pushButton(Button::B);}
  if(data == 102) {pushUpButton(Button::B);}
  if(data == 3) {pushButton(Button::A);}
  if(data == 103) {pushUpButton(Button::A);}
  if(data == 4) {pushButton(Button::X);}
  if(data == 104) {pushUpButton(Button::X);}
  if(data == 5) {pushButton(Button::L);}
  if(data == 105) {pushUpButton(Button::L);}
  if(data == 6) {pushButton(Button::R);}
  if(data == 106) {pushUpButton(Button::R);}
  if(data == 7) {pushButton(Button::ZL);}
  if(data == 107) {pushUpButton(Button::ZL);}
  if(data == 8) {pushButton(Button::ZR);}
  if(data == 108) {pushUpButton(Button::ZR);}
  if(data == 9) {pushButton(Button::MINUS);}
  if(data == 109) {pushUpButton(Button::MINUS);}
  if(data == 10) {pushButton(Button::PLUS);}
  if(data == 110) {pushUpButton(Button::PLUS);}
  if(data == 11) {pushButton(Button::LCLICK);}
  if(data == 111) {pushUpButton(Button::LCLICK);}
  if(data == 12) {pushButton(Button::RCLICK);}
  if(data == 112) {pushUpButton(Button::RCLICK);}
  if(data == 13) {pushButton(Button::HOME);}
  if(data == 113) {pushUpButton(Button::HOME);}
  if(data == 14) {pushButton(Button::CAPTURE);}
  if(data == 114) {pushUpButton(Button::CAPTURE);}
  
  if(data == 15) {pushHat(Hat::UP);}
  if(data == 115) {pushUpHat(Hat::UP);}
  if(data == 16) {pushHat(Hat::UP_RIGHT );}
  if(data == 116) {pushUpHat(Hat::UP_RIGHT );}
  if(data == 17) {pushHat(Hat::RIGHT );}
  if(data == 117) {pushUpHat(Hat::RIGHT );}
  if(data == 18) {pushHat(Hat::DOWN_RIGHT );}
  if(data == 118) {pushUpHat(Hat::DOWN_RIGHT );}
  if(data == 19) {pushHat(Hat::DOWN );}
  if(data == 119) {pushUpHat(Hat::DOWN );}
  if(data == 20) {pushHat(Hat::DOWN_LEFT );}
  if(data == 120) {pushUpHat(Hat::DOWN_LEFT );}
  if(data == 21) {pushHat(Hat::LEFT );}
  if(data == 121) {pushUpHat(Hat::LEFT );}
  if(data == 22) {pushHat(Hat::UP_LEFT );}
  if(data == 122) {pushUpHat(Hat::UP_LEFT );}
  if(data == 23) {pushHat(Hat::NEUTRAL );}
  if(data == 123) {pushUpHat(Hat::NEUTRAL );}

  if(data == 200) {
    leftX = Serial1.read();
    leftY = Serial1.read();
    tiltLeftStick(leftX, leftY);
    }  
    if(data == 201) {neutralLeftStick();}
  if(data == 202) {
    rightX = Serial1.read();
    rightY = Serial1.read();
    tiltRightStick(rightX, rightY);
    }
    if(data == 203) {neutralRightStick();}
}

// void setControllerStates() {
//   pushButton(Button::A);
//   pushUpButton(Button::A);
// }
void loop() {
  /* When received signals */
  if(Serial1.available()) {
    int c = Serial1.read();
    setControllerStates(c);
  }
  else{
  }
}
