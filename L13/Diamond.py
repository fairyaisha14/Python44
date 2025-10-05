#Write a program to demonstrate the numbers in a diamond pattern?
#take input from user 
rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0: #conditions
    halfDiaRow = int(rowSize/2)
else:
    halfDiaRow = int(rowSize/2)+1
space = halfDiaRow
#loop for upper part
for i in range(1, halfDiaRow=1): #loop for rows
    for j in range(1, space + 1):#loop for columns
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
    #incermenting number at each column
    num = num + 1
print()
space = 1
#loop for lower part
for i in range(1, halfDiaRow): #loop for rows
    for j in range(1,space+1): #loop for columns
        print(end=" ")
    space = space + 1
    num = 1
    for j in range (1,2*(halfDiaRow - 1)):
        print(end=str(num))
        num = num+1
    print()
