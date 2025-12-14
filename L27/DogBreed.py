class Dogs:
    species = "mammal"

    def __init__(self, type, age):
        self.type = type
        self.age = age


dog1 = Dogs("poodle", 3)  
dog2 = Dogs("German shepherd", 5)  


print("Jess is a {} who is {} years old".format(dog1.type, dog1.age))
print("Bingo is a {} who is {} years old".format(dog2.type, dog2.age))
