#Create a python program to create a flashcard using object-oriented programming. A flashcard is a two-sided card with information on both sides that can assist memory. A question and an answer are usually printed on one side of a flashcard. Follow these steps to complete the activity - 1. From the user, take the input for a word and its definition. 2. To assign values for Word and Meaning, create a class called flashcard and use the __init__() function. 3. We'll use the __str__() function to get a string with the term and its definition. 4. Save the strings that have been returned in a list. 5. To print all of the stored flashcards, use a while loop.

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):

        #we willl return a string
        return self.word+' ('+self.meaning+' )'
    
flash = []
print("Welcome to flashcard application")

# the following loop will be repeated until user stops to add the flashcards
while(True):
    word = input("Enter the name you want to add to flashcard")
    meaning = input("Enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard otherwise enter 1 : "))

    if (option):
        break

#printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">", i)