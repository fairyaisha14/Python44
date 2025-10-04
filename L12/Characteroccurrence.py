#take input of a word
string = input("Please enter your own word : ")
#take input of a character
char = input("Please enter your own Character : ")
i = 0
count = 0
#loop will to find the occurance of a character
while (i < len(string)): #string operation
    
    if(string[i] == char): #condition 1
        count = count + 1
    i = i + 1
    
#Display the result
print("The total number of times ", char, "has occured = ", count)