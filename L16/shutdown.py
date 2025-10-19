import os

answer = input("Are you done with this app? ")

if answer.lower() == "yes":
    os.system("taskkill /IM Code.exe /F")
else:
    print("Okay, happy coding!")