#parent class
class Animal:
    def speak(self):
        print("Animal is speaking")


#child class
class Dog(Animal): #dog is inheriting propertise of the animal
    def bark(self):
        print("Dog is barking")

#objects
a = Animal()
a.speak()

b = Dog()
b.bark()
b.speak()
