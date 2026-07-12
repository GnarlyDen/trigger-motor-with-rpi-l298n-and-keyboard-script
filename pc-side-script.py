import keyboard
import serial

# keyboard.wait('space')

# this basically opens the connection between the pc and the raspberry pi
# 
# rpi_port = serial.Serial('COM3', 115200)

def on_press(event):
    print(event)

def on_release(event):
    print(event)

keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait()