"""
students={'student1':{'name':'John','rollNo':101,'percent':88},
          'student2':{'name':'Van dijk','rollNo':102,'percent':78},
          'student3':{'name':'Ronaldo','rollNo':103,'percent':94}}
print(type(students))

with open("student_info.txt",'wt') as fh:
    fh.write(str(students))          


with open("student_info.txt",'rt') as fh:
    print(fh.read())
    print(type(fh.read()))
"""
# if we want to change it into dict we can't that where pickle is used

import pickle
students={'student1':{'name':'John','rollNo':101,'percent':88},
          'student2':{'name':'Van dijk','rollNo':102,'percent':78},
          'student3':{'name':'Ronaldo','rollNo':103,'percent':94}}
print(type(students))
'''
# serialization
with open("student.bin",'bx') as fh:
    for i in students:
        pickle.dump(students[i],fh)
'''
# deserialization
with open("student.bin",'rb') as fh:
    while True:
        try:
            data=pickle.load(fh)
            if data['percent']>90:
                print(data,type(data))
        except EOFError:
            print("You're Done!!") 
            break   