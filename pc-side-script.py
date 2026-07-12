import keyboard
import serial
import time

time.sleep(.1)
# keyboard.wait('space')

# this opens the connection between the pc and the raspberry pi
# rpi_port = serial.Serial('COM7', 9600)

# ser = serial.Serial('/dev/ttyUSB0')

def on_press(event):
    print(event.name)

def on_release(event):
    print(event.name)

keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait()