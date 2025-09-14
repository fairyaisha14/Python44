a = 12
b = 3
c = 4
d = 9
answer = b**c + d/ b*c + a
print(answer)



n1 = int(input("enter numerator"))
n2 = int(input("enter denominator"))
if n1 % n2==0:
    print(str(n1)+ " is divisible by "+str(n2))
else:
    print(str(n1)+ " is not divisible by "+str(n2))