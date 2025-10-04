num = int(input("Enter a number from 1 to 10: "))

if 1 <= num <= 10:
    for power in range(1, 11):
        result = num ** power
        print(f"{num} to the power of {power} is {result}")
else:
    print("Please enter a number between 1 and 10.")