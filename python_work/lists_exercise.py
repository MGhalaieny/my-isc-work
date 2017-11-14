#List exercises

mylist = [1,2,3,4,5]

print mylist[1]
print mylist[-2]
print mylist[0:5] #All items in the list
print mylist[1:4] #Second to fourth items in list

#Create a list from a range and play with it

one_to_ten = range(1,11) 
print one_to_ten
one_to_ten[0] = 10 #replace first element with 10
print one_to_ten
one_to_ten.append(11) #append 11 to list
print one_to_ten
one_to_ten.extend([12,14])
print one_to_ten

#Combining lists and loops

forward = []
backward =[]

values = ["a", "b", "c"]

for letter in values:
    forward.append(letter)   
    backward.insert(0,letter)

print forward
print backward

forward.reverse()
print forward
print forward == backward

#Other list exercises

countries = ["UK", "USA", "UK", "UAE"]

dir(countries)

#help(countries.count)

print countries.count("UK")





