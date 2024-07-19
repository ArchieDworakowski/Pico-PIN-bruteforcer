import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time


#Function to convert number string to keyboard input
def presser(key):
    if key == "0":
        kbd.send(Keycode.ZERO)
    if key == "1":
        kbd.send(Keycode.ONE)
    if key == "2":
        kbd.send(Keycode.TWO)
    if key == "3":
        kbd.send(Keycode.THREE)
    if key == "4":
        kbd.send(Keycode.FOUR)
    if key == "5":
        kbd.send(Keycode.FIVE)
    if key == "6":
        kbd.send(Keycode.SIX)
    if key == "7":
        kbd.send(Keycode.SEVEN)
    if key == "8":
        kbd.send(Keycode.EIGHT)
    if key == "9":
        kbd.send(Keycode.NINE)


#Opening list of combination
f = open("combos.txt","r")

#Initialize the Keyboard HID
kbd = Keyboard(usb_hid.devices)






for x in f:
    for y in x:
        presser(y)
        time.sleep(0.75)

    kbd.send(Keycode.ENTER)
exit()

000