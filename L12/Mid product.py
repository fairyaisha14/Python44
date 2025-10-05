# Input a number
num = int(input("Enter the number: "))
t = num
numLen = 0

# Count the number of digits
while t > 0:
    numLen += 1
    t = int(t / 10)

# Check if number has 4 or more digits
if numLen >= 4:
    midPos = int(numLen / 2)
    chk = 0
    midOne = midTwo = 0
    temp = num

    # Extract digits from right to left
    while temp > 0:
        rem = temp % 10
        if chk == midPos:
            midOne = rem
        elif chk == (midPos - 1):
            midTwo = rem
        temp = int(temp / 10)
        chk += 1

    prod = midOne * midTwo
    print(f"\nProduct of Mid digits ({midOne} * {midTwo}) = {prod}")
else:
    print("\nIt's not a 4 or more than 4-digit number!")