"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.

class Animal:

    def __init__(self, species, age, habitat, diet):
        self.species = species
        self.age = age
        self.habitat = habitat 
        self.diet = diet
    
    def eat(self):
        return f"{self.species} is munchin"
    def sleep(self):
        return f"{self.species} be sleepin"
    



# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.
class Mammal(Animal):
    
    def __init__(self, species, age, habitat, diet, hairs):
        super().__init__(species, age, habitat, diet)
        self.hairs = hairs
    
    def grow_hair(self):
        return f"{self.species}'s hair do be growin"
    
    def __str__(self):
        return f"{self.species} that is {self.age} years old, live in a {self.habitat} is a {self.diet} and has {self.hairs} hairs"
class Fish(Animal):
    def __init__(self,species, age, habitat, diet, legs):
        super().__init__(species, age, habitat, diet)
        self.legs = legs
    
    def walk(self):
        return f" {self.species} is trying their best however is a fish"
   
    def __str__(self):
        return f"{self.species} that is {self.age} years old, live in a {self.habitat} is a {self.diet} and has {self.legs} legs"





# Create at least two instances of the Animal derived classes with different data.
Kyle = Fish("Mullet", 10, "Water","Omnivor", 3)
Cyle = Mammal("Elephant", 100, "Plains","Herbivor", 30000)




# Write code that prints out the details of each animal and calls their specific behaviors.
print(Kyle)
print(Cyle)
print(Kyle.walk())


