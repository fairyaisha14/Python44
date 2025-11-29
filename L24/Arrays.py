#Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3]. Then find the number of occurrences of number 3 in the array. Also, print the reversed array.
import array as arr

# create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:"+str(array_num))

#count number of occurences
print("Number of occrrences of the number 3 in the said array:"+str(array_num.count(3)))

# reverse the array
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))