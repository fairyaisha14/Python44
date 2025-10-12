#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly
def add (P, Q):
    #This function is used for adding two numbers
    return P + Q
def subtarct(P, Q):
    #This function is used for subtracting two numbers
    return P - Q
def multiply(P, Q):
    #This function is used for multiplying two numbers
    return P * Q
def divide (P, Q):
    #This function is used for dividing two numbers
    return P / Q
#Now we will take input from the user 
print ("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Please enter choice (a/b/c/d):")
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: ")) 

if choice =='a':
    print(num_1, "+", num_2)


