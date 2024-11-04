#Polymorphism in Python is a concept that allows objects of
# different classes to be treated as objects of a common superclass.
class Rectangle:
    def shape(self):
        print("draw the rectangle")

class Parallelogram:
    def shape(self):
        print("draw the parallelogram")

class Rhombus:
    def shape(self):
        print("draw the rhombus")

r = Rectangle()
r.shape()

p = Parallelogram()
p.shape()

rhom = Rhombus()
rhom.shape()