class Student:
    pass

s1=Student()
s2=Student()

s1.name="John"
s1.marks=85

print(s1.name)
print(s1.marks)

help(Student)

print(s1.__dict__)