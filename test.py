import serial
import time

time.sleep(.1)

port_from_computer = serial.Serial('COM6', 9600, write_timeout=1)

while True:
    print(port_from_computer.read(1))