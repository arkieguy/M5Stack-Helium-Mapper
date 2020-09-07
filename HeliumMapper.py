from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)




label0 = M5TextBox(0, 125, "Helium", lcd.FONT_Default,0x05f5ff, rotate=0)
LoRaConnectCount = M5TextBox(253, 147, "0", lcd.FONT_Default,0x099faa, rotate=0)
LoraStatus = M5TextBox(0, 175, "_", lcd.FONT_Default,0x099faa, rotate=0)
title0 = M5Title(title="               Helium Coverage Mapper", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label1 = M5TextBox(0, 26, "GPS Information:", lcd.FONT_Default,0x37ff04, rotate=0)
Time = M5TextBox(252, 29, "00:00:00", lcd.FONT_Default,0x2dab07, rotate=0)
Label_lat = M5TextBox(0, 50, "Lattitude: ", lcd.FONT_Default,0x2dab07, rotate=0)
lat = M5TextBox(88, 49, "000.0000", lcd.FONT_Default,0x2dab07, rotate=0)
label2 = M5TextBox(0, 152, "LoRaWan Response:", lcd.FONT_Default,0x099faa, rotate=0)
label3 = M5TextBox(0, 69, "Longitude: ", lcd.FONT_Default,0x2dab07, rotate=0)
long = M5TextBox(88, 69, "000.0000", lcd.FONT_Default,0x2dab07, rotate=0)

from numbers import Number

string = None
DevEui = None
AppEui = None
AppKey = None
count = None

def cmd(string):
  global DevEui, AppEui, AppKey, count
  uart1.write(str(string)+"\r\n")
  string = wait4Reply()

def wait4Reply():
  global string, DevEui, AppEui, AppKey, count
  while not (uart1.any()):
    wait_ms(250)
    if btnC.isPressed():
      break
  string = uart1.read()
  LoraStatus.setText(str(string))
  if str(string).count('ERROR') > 0:
    wait(10)
  return string

def Connect2Helium(DevEui, AppEui, AppKey):
  global string, count
  cmd('AT+RESET')
  wait(2)
  cmd('AT+ID=DevEui,"{DevEUI}"'.replace('{DevEUI}', DevEui))
  cmd('AT+ID=AppEui,"{AppEUI}"'.replace('{AppEUI}', AppEui))
  cmd('AT+KEY=AppKey,"{AppKey}"'.replace('{AppKey}', AppKey))
  cmd('AT+DR=US915')
  cmd('AT+CH=0,903.9,DR0,DR3')
  cmd('AT+CH=1,904.1,DR0,DR3')
  cmd('AT+CH=2,904.3,DR0,DR3')
  cmd('AT+CH=3,904.5,DR0,DR3')
  cmd('AT+CH=4,904.7,DR0,DR3')
  cmd('AT+CH=5,904.9,DR0,DR3')
  cmd('AT+CH=6,905.1,DR0,DR3')
  cmd('AT+CH=7,905.3,DR0,DR3')
  cmd('AT+CH=8,904.6,DR4')
  cmd('AT+POWER=20')
  cmd('AT+ADR=OFF')
  cmd('AT+DR=DR3')
  cmd('AT+CLASS=A')
  string = 'Join failed'
  count = 0
  while string.count('Join failed') > 0:
    count = (count if isinstance(count, Number) else 0) + 1
    LoRaConnectCount.setText(str(count))
    cmd('AT+Join')
    string = str(wait4Reply())
    if btnC.isPressed():
      break
  wait(5)



uart1 = machine.UART(1, tx=17, rx=16)
uart1.init(9600, bits=8, parity=None, stop=1)
Connect2Helium('', '', '')
cmd('AT+MSG="Test"')
string = str(wait4Reply())
wait(5)
cmd('AT+MSG="Test"')
string = str(wait4Reply())
