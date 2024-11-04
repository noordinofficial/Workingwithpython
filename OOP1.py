#class is a blue print of an object
#object is an instance of a class
#propertis is characteristic of the class and the object

class Student :
    #propertise/Attributes
    name = "Nurdin"
    age = 21

    #Behaviours / Methods / Functions
    def Study(self):
        print("student is studying")

student1 = Student() # instantiating / creating object
student1.Study()

student2 = Student()


print(student1.name)

