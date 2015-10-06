#!/usr/bin/python

import sys
import serial
import time

msgs = []
msgs.append("/ISk5\2ME382-1003\r\n\
\r\n\
0-0:96.1.1(4B413650303035313232373630303132)\r\n\
1-0:1.8.1(00036.133*kWh)\r\n\
1-0:1.8.2(00017.004*kWh)\r\n\
1-0:2.8.1(00000.002*kWh)\r\n\
1-0:2.8.2(00000.003*kWh)\r\n\
0-0:96.14.0(0002)\r\n\
1-0:1.7.0(0000.01*kW)\r\n\
1-0:2.7.0(0000.04*kW)\r\n\
0-0:17.0.0(0999.00*kW)\r\n\
0-0:96.3.10(1)\r\n\
0-0:96.13.1()\r\n\
0-0:96.13.0()\r\n\
0-1:24.1.0(3)\r\n\
0-1:96.1.0(3238313031353431303038373537353132)\r\n\
0-1:24.3.0(130110100000)(00)(60)(1)(0-1:24.2.1)(m3)\r\n\
(00001.160)\r\n\
0-1:24.4.0(1)\r\n\
!\r\n")

msgs.append(
"/ISk5\2MT382-1003\r\n\
\r\n\
0-0:96.1.1(5A424244303035313330323736353132)\r\n\
1-0:1.8.1(00001.572*kWh)\r\n\
1-0:1.8.2(00000.642*kWh)\r\n\
1-0:2.8.1(00000.002*kWh)\r\n\
1-0:2.8.2(00000.001*kWh)\r\n\
0-0:96.14.0(0002)\r\n\
1-0:1.7.0(0000.03*kW)\r\n\
1-0:2.7.0(0000.08*kW)\r\n\
0-0:17.0.0(0999.00*kW)\r\n\
0-0:96.3.10(0)\r\n\
0-0:96.13.1()\r\n\
0-0:96.13.0()\r\n\
0-1:24.1.0(3)\r\n\
0-1:96.1.0(3238313031353431303036353936353132)\r\n\
0-1:24.3.0(130110110000)(00)(60)(1)(0-1:24.2.1)(m3)\r\n\
(00001.456)\r\n\
0-1:24.4.0(0)\r\n\
!\r\n")


if __name__ == "__main__":
    ############################################################################

    port = sys.argv[1]

    serial_port = serial.Serial(port, 9600, bytesize=7, parity=serial.PARITY_NONE, stopbits=2)
    #serial_port = serial.Serial(port, 115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1)
    print "Opened:", serial_port.name

    i = 0
    while True:
        print "Send:", msgs[i]
        serial_port.write(msgs[i])
        time.sleep(10)
        i += 1
        i = i % len(msgs)
