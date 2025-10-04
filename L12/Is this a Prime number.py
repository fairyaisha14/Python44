#take two input from user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter an upper range: "))


print("Prime numbers between", lower, "and", upper, "are:")
#iterate loop from lower imit to upper limit
for num in range(lower, upper +1):
    # all prime numbers are graeter than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)