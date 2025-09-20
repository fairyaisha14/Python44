 #Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.

# #Take input for the student that he can attend the exam or not

medical_cause=input("did you hav a medical cause Y or N: ")


atten = int(input("enter the attendance of the student:  "))

#checking the user input predicting output accordingy

if medical_cause == 'Y':
   print ("You are allowed")
else:
   if atten>=75:
     print ("Allowed")
   else:
     print("Not Allowed")
