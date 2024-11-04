
class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("person is moving")

#a,b,c are object
a = Person("Nurdin",34,"Male")
print(a.name,a.age,a.gender)

b = Person("Ali",22,"Male")
print(b.name,b.age,b.gender)

c = Person("Marry",19,"Female")
print(c.name,c.age,c.gender)




