import serial
import time
import sys

cmd1 = 'cat /etc/issue'
cmd2 = 'devmem 0xff9c00c4'
cmd3 = 'cat /mnt/factory/configs/unit/hwid.txt'
cmd4 = 'dapd -sq'

COM = 'COM15'

try:
    ser = serial.Serial(
        port=COM,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
        xonxoff=False,
        rtscts=False,
        dsrdtr=False,
        writeTimeout=2
    )
except:
    print 'Port blocked'
    print sys.exc_info()[0]


# time.sleep(3)

# if ser.is_open:
#	print '%s port oppened' % COM

def call(cmd):
    ser.write(cmd + '\n')
    response = ser.readlines()
    return response


if ser.is_open:
    print call(cmd1)[10]
    print call(cmd2)[1]
    print call(cmd3)[1]
    print call(cmd4)[8]
    ser.close()

time.sleep(1)

raw_input("Press enter to continue:  ")