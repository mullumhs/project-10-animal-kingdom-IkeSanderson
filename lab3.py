"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Build a Zoo class to manage a collection of animals from the Animal
               Kingdom program. Demonstrate managing objects and class interactions.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Import your base class Animal and any derived classes (e.g., Bird, Fish) here from Lab 2.

from lab2 import Animal, Fish, Mammal


# Define the Zoo class that can manage multiple Animal objects. It should have the following two methods:
# __init__ - Initialises a new Zoo instance with an empty list to hold animal objects.
# add_animal - Adds an animal to the zoo's list and confirms addition with a return message.
# You should then think of and implement at least one additional method for the Zoo class. E.g. feed_all

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.species} Has been added to the Zoo")
   
    def feed(self):
        for animal in self.animals:
            print(f"Feeding {animal.species}")




# Create instances of derived Animal classes and add them to the Zoo.
zoo = Zoo()
zoo.add_animal(Fish("Mullet", 10, "Water","Omnivor", 3))
zoo.add_animal(Mammal("Elephant", 100, "Plains","Herbivor", 30000))



# Demonstrate the Zoo's functionality by calling its methods.
zoo.feed()




