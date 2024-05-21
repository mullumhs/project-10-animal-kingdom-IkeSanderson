"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the Animal Kingdom program from Lab 1 to include polymorphism,
               demonstrating method overriding in derived classes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Paste your base class Animal and the derived classes from Lab 1 here.

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
    
    def __str__(self):
        return f"{self.species} that is {self.age} years old, live in a {self.habitat} is a {self.diet}"
    
    def walk(self):
        return f"{self.species} is walking"

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
        return f"{self.species} is trying their best however is a fish"
   
    def __str__(self):
        return f"{self.species} that is {self.age} years old, live in a {self.habitat} is a {self.diet} and has {self.legs} legs"


Mullet = Fish("Mullet", 10, "Water","Omnivor", 3)
Elephant = Mammal("Elephant", 100, "Plains","Herbivor", 30000)

print(Elephant.walk())
print(Mullet.walk())
# Modify the classes to demonstrate polymorphism through method overriding.
# Each derived class should override at least one method from the Animal class.
# For instance, you might want to override a 'make_sound' method to reflect the specific sound each animal makes.





# Create at least two instances of your derived classes





# Call the overridden methods on the instances.




