import sys

name = input("What is your name? ")
print("Hello", name)

response = input("Have you completed an achievement? (yes/no): ")

if response.lower() == "yes":
    achievement = input("What is your achievement? ")
else:
    print("Come back next time to celebrate your goals!")
    sys.exit()

print(f"CONGRATULATIONS FOR {achievement.upper()}!")





A

  