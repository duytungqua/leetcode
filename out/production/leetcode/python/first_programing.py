#print

print("Hello World")

#variable
a = 10
name = "string"
age = 20 
height = 5.5 # float
is_student = False

print(a, name, age, height, is_student)

#condition
if age > 18:
    print("You are adult")
elif age == 18:
    print("You are 18")
else:
    print("You are not adult")

#loop
for i in range(10):
    print(i)
#while loop
i = 0 
while i < 10:
    print(i)
    i += 1

#function
def add(a, b):
    return a + b

#arr
arr = [1,2,3,4]
print(arr[1])

arr_2d = [
    [1, 2, 3],
    [4,5,6]
    ]
print(arr_2d[1][2])

#constant
PI = 3.14
#constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
p1 = Person("John", 36)
print(p1.get_name())