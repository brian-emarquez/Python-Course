# Python code to demonstrate namedtuple()
from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
request = Student('brian', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(request[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(request.name)