import time
time.sleep(0.1) # waits for USB to become ready

from machine import Pin
import sys
import select

#configures the pins control whether 
#the motor moves forwards or backwards
in1 = Pin(1, Pin.OUT)
in2 = Pin(2, Pin.OUT)

#stops the motor
def stop():
    in1.value(0)
    in2.value(0)

#self-explanatory
def backwards():
    in1.value(0)
    in2.value(1)

def forwards():
    in1.value(1)
    in2.value(0)

#triggers the motor to move back or forth after 'w'
#or 's' are pressed
# 'w' is forwards, 's' is backwards
def trigger_motor(key_input):
    if key_input == 's':
        backwards()

    if key_input == 'w':
        forwards()

    if key_input == 'r':
        stop()

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

while True:
    #time.sleep(.5)
    events = poll.poll(0)
    
    if events:
        try:
            key_from_pc = sys.stdin.read(1)
            trigger_motor(key_from_pc)

        except:
            pass