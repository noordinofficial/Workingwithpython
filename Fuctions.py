# Build-in library functions

y = max(56,78,90,23,12)
print("the maximum value is :",y)

x= min(67,78,12,98)
print("the minimum value is  :",x)

z = pow(2,3)
print("the result is : ", z)

#User-defined functions
def greeting ():
    print("Hello there! " )
greeting() # this is calling a function

def Multiply ():
    num1 = 11
    num2 = 23
    print(num1*num2)
Multiply()

# Parameters/variable and argument/values

def Add(a,b):
    print(a+b)

Add(43,11)
Add(11,12)
Add(90,100)


def Employee(FullName,Age, Position,Status):
    print(FullName,Age,Position,Status)

Employee("Nurdin Abdi","25","CEO","Married")
Employee("Hussein Muhamud","22","HR","Married")

















