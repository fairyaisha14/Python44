#Write a program to calculate the number of notes in the given amount?

# Taking total amount as input from user
Amount = int(input("Please enter amount for withdraw :"))

#Calculating the number of notes of different denominations
note_1 = Amount//50
note_2 = (Amount%50)//20
note_3 = ((Amount%50)%20)//10
note_4 = (((Amount%50)%20)%10)//5


print("notes of 50 pounds" , note_1)
print("notes of 20 pounds" , note_2)
print("notes of 10 pounds" , note_3)
print ("notes of 5 pounds" , note_4)