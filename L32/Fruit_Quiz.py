#Write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of - 1. a constructor with a dictionary of fruits and respective colours 2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.

import random
class FruitQuiz:

    # Create a constructor
    def __init__(self):

        #Create a dictionary of fruits as keys and color as value
        self.fruit={'apple':'red',
                    'orange':'orange',
                    'watermelon':'green',
                    'banana':'yellow'}
        
    #Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruits.items()))

            print("What is the color of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct answer")

            else:
                print("Wrong answer")

            option = int(input("Enter 0 , if you want to play again otherwise enter 1: "))
            if (option):
                break

            print("Welcome to fruit quiz ")
            fq = FruitQuiz()
            fq.quiz()


            