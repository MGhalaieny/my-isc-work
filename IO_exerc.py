#IO exercise

#1 Read entire contents of CSV file and display each line

with open('weather.csv') as reader:
    data = reader.read()
    print data

print "End of exercise 1\n"

#2 Read the file line by line

print "Begin exercise 2\n"

with open('weather.csv') as reader:
    line = reader.readline()
    while line:
        print line
        line = reader.readline()

print "It's over\n"

#3 Grab rainful values

print "Begin exercise 3\n"

with open('weather.csv') as reader:
    line = reader.readline()
    rain = []
    for line in reader.readlines():
        print line
        r = line.strip().split(",")[-1]
        r = float(r)
        rain.append(r)

print rain

with open ("myrain.txt", "w") as writer:
    for r in rain:
        writer.write(str(r) + "\n")

print "End exercise 3\n"

#4 Write and read binary values

import struct

bin_data = struct.pack("bbbb", 123, 12, 45, 34)

with open ("mybinary.dat", "wb") as bwriter:
    bwriter.write(bin_data)


