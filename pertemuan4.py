from abc import ABC, abstractmethod

class Animal(ABC):
    def speak(self):
        pass
    def foot(self):
        pass

class Dog(Animal):
    def speak (self):
        return "Bark!"
    def foot(self):
        return 4
    
class Chicken(Animal):
    def speak(self):
        return "chick-chick!"
    def foot(self):
        return 2
    


#absctarct
#dog = Dog()
#chicken = Chicken()

#print("sound of the dog :" + dog.speak()+"Dog Has :" + str(dog.foot()) +"foot" + chicken.speak() +"Chicken HAS :" + str(chicken.foot()) + "foot")

def animal_behavior(animal: Animal):
    print(f"the animal says: {animal.speak()}")
    print(f"the animal has:" + str(animal.foot())+ "legs")

dog = Dog();
chicken = Chicken();

animal_behavior(dog);
animal_behavior(chicken);