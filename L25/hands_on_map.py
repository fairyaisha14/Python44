#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
#Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print ("Addition of two lists: ")
print(list(result))
#using map
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list")
print(square)