# Data Structure- is a multiple values stored in a single variable

#List is ordered and changeable
Cars= ["Toyota", "Honda", "Nissan", "BMW", "Audi" ]

#Tuple is ordered and unchangeable
Fruits = ("Banana", "Apple", "Orange", "Grape", "Strawberry")

#Set is unordered and unchangeable
Countries= {"Kenya", "Uganda", "Tanzania"}

#Dictonary is a key and a value pair
Student ={
    "StudentID :" : 66495,
    "FirstName": "Nurdin",
    "LastName": "Yussuf",
    "Age" : 24,
    "course" : "Web Development",
    "Nationality" : "Kenyan"
}
print(Cars)
print(Fruits)
print(Countries)
print(Student)
print(Student["Nationality"])

#Determining the type of datatype
print(type(Cars))
print(type(Fruits))
print(type(Countries))
print(type(Student))
