
courses = ["IST","Cybersecurity","DataScience"]
print(courses)

#accessing an element in ana array
print(courses[0])
print(courses[1])
print(courses[2])


#looping through an array
for y in courses:
    print("course ", y)

#Adding new element in an array - use .append method to do this
courses.append("Python")
print(courses)


#removing an element from an array - use the .remove method
courses.remove("Python")
print(courses)


