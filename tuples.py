#working with tuples

#1 create a couple of tuples

t=(1,)

print t[-1]


bigtuple = range(100,201)
tuple(bigtuple)
print bigtuple[0]
print bigtuple[-1]
print bigtuple

#2 enumeration

mylist = [23, "hi", 2.4e-10]
for (count, item) in enumerate(mylist):
    print count, item

#3 unpacking 

first, middle, last = mylist
print first, middle, last
first, middle, last = middle, last, first
print first, middle, last






