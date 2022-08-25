import digitalio
import board
import usb_hid
import time
import rotaryio
from digitalio import DigitalInOut, Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("== Pi Pico multifunction knob 1.0 =="), print("---Pico Pad Keyboard---")

# Rotary encoder 1
enc = rotaryio.IncrementalEncoder(board.GP0, board.GP1)
encSw = digitalio.DigitalInOut(board.GP7)
encSw.direction = digitalio.Direction.INPUT
encSw.pull = digitalio.Pull.UP
lastPosition = 0

# Rotary encoder 2
#enc2 = rotaryio.IncrementalEncoder(board.GP2, board.GP3)
#enc2Sw = digitalio.DigitalInOut(board.GP8)
#enc2Sw.direction = digitalio.Direction.INPUT
#enc2Sw.pull = digitalio.Pull.UP

# Rotary encoder 3
#enc3 = rotaryio.IncrementalEncoder(board.GP4, board.GP5)
#enc3Sw = digitalio.DigitalInOut(board.GP9)
#enc3Sw.direction = digitalio.Direction.INPUT
#enc3w.pull = digitalio.Pull.UP

# Rotary encoder 4
#enc4 = rotaryio.IncrementalEncoder(board.GP21, board.GP20)
#enc4Sw = digitalio.DigitalInOut(board.GP10)
#enc4Sw.direction = digitalio.Direction.INPUT
#enc4Sw.pull = digitalio.Pull.UP

# Media buttons
btnStop = digitalio.DigitalInOut(board.GP11)
btnStop.direction = digitalio.Direction.INPUT
btnStop.pull = digitalio.Pull.UP

btnPrev = digitalio.DigitalInOut(board.GP9)
btnPrev.direction = digitalio.Direction.INPUT
btnPrev.pull = digitalio.Pull.UP

btnPlay = digitalio.DigitalInOut(board.GP13)
btnPlay.direction = digitalio.Direction.INPUT
btnPlay.pull = digitalio.Pull.UP

btnNext = digitalio.DigitalInOut(board.GP14)
btnNext.direction = digitalio.Direction.INPUT
btnNext.pull = digitalio.Pull.UP

# builtin LED
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

# USB device
consumer = ConsumerControl(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

# button delay
dl = 0.2

# loop
while True:
    # poll encoder position
    position = enc.position
    if position != lastPosition:
        led.value = True
        if lastPosition < position:
            Keyboard(usb_hid.devices).send(0, Keycode.LEFT_ARROW)
        else:
            Keyboard(usb_hid.devices).send(0, Keycode.RIGHT_ARROW)
        lastPosition = position
        led.value = False
    
    # poll encoder button
    if encSw.value == 0:
        keyboard.send(Keycode.CONTROL, Keycode.K)
        led.value = True
        time.sleep(dl)
        led.value = False
    
    # poll media buttons
    if btnStop.value == 0:
        Keyboard(usb_hid.devices).send(0, Keycode.A)
        led.value = True
        time.sleep(dl)
        led.value = False
        
    if btnPrev.value == 0:
        Keyboard(usb_hid.devices).send(0, Keycode.B)
        led.value = True
        time.sleep(dl)
        led.value = False
        
    if btnPlay.value == 0:
        Keyboard(usb_hid.devices).send(0, Keycode.C)
        led.value = True
        time.sleep(dl)
        led.value = False
        
    if btnNext.value == 0:
        Keyboard(usb_hid.devices).send(0, Keycode.D)
        led.value = True
        time.sleep(dl)
        led.value = False
        
    time.sleep(0.1)