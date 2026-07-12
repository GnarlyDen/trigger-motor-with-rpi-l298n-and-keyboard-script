
import serial
rpi_port = serial.Serial('COM*', 9600)
ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device, p.description)

devices = [port.device for port in serial.tools.list_ports.comports()]
ports = [port for port in devices]
#if len(ports) != 1:
    #raise Exception('cannot identify port to use'

print(devices, ports)