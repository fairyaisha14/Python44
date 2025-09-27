
age = int(input("How old are you?"))  # Convert input to integer

if (age >= 5) and (age <= 10):
    print("You are still a young child")
elif (age >= 11) and (age <= 20):
    print("You are a teenager")
elif (age >= 21) and (age <= 35):
    print("You are a young adult")
elif (age >= 36) and (age <= 49):
    print("You are an adult")
elif (age >= 50) and (age < 60) :
    print("You are middle age ")
else:
    print("You are quite old")
