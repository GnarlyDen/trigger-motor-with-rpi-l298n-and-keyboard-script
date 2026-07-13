first, connect the raspberry pi to your computer
make sure the pi, motor, and the wiring is done well also
also, idk how to do this since it's up to you,
but load the 'rpi-side-script.py' into the raspberry pi...

anyways,
write this in the terminal and then press enter:
    "py list-ports.py"
and, if the raspberry pi is connected, the terminal should list 
the port which the pi is connected to (and maybe other ports)

the response should look like:
    "USB Serial Device (COM#)"
or it could look like
    "COM# - Board CDC (COM#)"
(# is a placeholder for a number btw)

the number which is in place of the # sign when you run this command
should be added in the file called:
    "pc-side-script.py"

look at line 13, where it says:
    "rpi_port = serial.Serial('COM8', 9600)"
change the number 8 ("COM8") into what ever the number from earlier is

now, you can run this script.
type "py pc-side-script.py" in the terminal and press enter

'w' to move forward
's' to move backward
'r' to stop the motor
escape key close the program.
(use these commands in the terminals)