#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple  
#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print (tuplex)

#create a tuple
tuplex = (4, 6, 2 ,8, 3, 1)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element aqnd it wil create a new tuple
tuplex = tuplex + (9,)
print (tuplex)
#Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#if the start index isn't defined, is taken from the beginning of the tuple
_slice = tuplex[:6]
print(_slice)