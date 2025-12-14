#Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)#
# create a class 
# create a class 
class pair_elements:

    def twoSum(self, nums, target):
        # create an empty dictionary
        lookup = {}

        # iterate through the tuple
        for i, num in enumerate(nums):
            # check if target - num is in the dictionary
            if target - num in lookup:
                # return the indices if a pair is found
                return (lookup[target - num], i)
            # add the current number and its index to the dictionary
            lookup[num] = i

# take input of num from user
value = int(input("Enter sum for which you want to make this search: "))

# create an instance of the pair_elements class and find the pair
print("index1=%d, index2=%d" % pair_elements().twoSum((10, 20, 30, 40, 50, 60, 70), value))
