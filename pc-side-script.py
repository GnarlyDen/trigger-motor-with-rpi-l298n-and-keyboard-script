import keyboard
import serial
import time

time.sleep(.1)
# defines the keys that'll be used to control the motor
control_keys = ('w', 's', 'r')
end_program_key = 'esc'
# this opens the connection between the pc and the raspberry pi
rpi_port = serial.Serial('COM8', 9600)
# ser = serial.Serial('/dev/ttyUSB0')

def on_press(event):
    if event.name in control_keys:
        key_released = event.name
        print(key_released)
        rpi_port.write(key_released.encode('utf-8'))

def on_release(event):
    if event.name in control_keys:
        rpi_port.write(b'r') 
        print('event.name')  

keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait(end_program_key)
# rpi_port.close()