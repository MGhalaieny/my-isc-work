#Exercise on strings

# Looping through a string

print "Exercise 1\n"
s = "I love to write python"

for char in s:
    print char

print s[4]
print s[-1]
print len(s)

#try printing
print s[0]
print s[0][0]
print s[0][0][0]

print "End Exercise 1\n"

#Splitting a string

print "Exercise 2\n"

s = "I love to write python"

s_split = s.split(" ")
print s_split

for word  in s_split:
    if word.find("i") > -1:
        print "I found 'e' in:", word


print "End Exercise 2\n"

# Other aspects 
print "Exercise 3\n"

something = "Completely Different"

print dir(something)

print something.count("t")

print something.find("plete")

split = something.split("e")
print split

thing2 = "Something Silly"




print "End Exercise 3\n"



