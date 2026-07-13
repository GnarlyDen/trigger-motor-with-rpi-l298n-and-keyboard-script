import keyboard
import serial
import time
import threading

stop_program_flag = threading.Event()
# time.sleep(.1)
# defines the keys that'll be used to control the motor
control_keys = ('w', 's', 'r')
end_program_key = 'esc'
# this opens the connection between the pc and the raspberry pi

rpi_port = serial.Serial('COM7', 9600, write_timeout=1)

def on_press(event):
    if event.name in control_keys:
        try:
            key_released = event.name
            print(event)
            rpi_port.write(key_released.encode('utf-8'))

        except serial.SerialTimeoutException:
            print('PC side timed out. \nIs the Raspberry Pi on and connected?')
            # keyboard.press(end_program_key)
            stop_program_flag.set()
            return


keyboard.on_press(on_press)
keyboard.add_hotkey(end_program_key, stop_program_flag.set)

stop_program_flag.wait()
rpi_port.close()