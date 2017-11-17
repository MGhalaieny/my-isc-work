#!/usr/bin/python2.7

import serial
import datetime
from datetime import datetime
import io

outfile='/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)


sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

with open(outfile, 'a') as f:
   while ser.isOpen():
       datastring=ser.read(size=8)
    #print datetime.datetime.utcnow().isoformat(), ser.read(size=8)
    #print "===="
  #      datastring = sio.readline()
   #     f.write(datetime.datetime.utcnow().isoformat() + '\t' + datastring + '\n')
    #    f.flush()
    #print datetime.datetime.utcnow().isoformat(), datastring
