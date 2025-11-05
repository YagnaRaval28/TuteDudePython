# javascript object notation- full form of json
import json
students={'student1':{'name':'John','rollNo':101,'percent':88,'sports':True},
          'student2':{'name':'Van dijk','rollNo':102,'percent':78,'sports':True},
          'student3':{'name':'Ronaldo','rollNo':103,'percent':94,'sports':True}}
print(students,type(students))
'''
with open("student.json",'w') as fh:
    json.dump(students,fh,indent=4)
'''
with open("student.json",'r') as fh:
    data=json.load(fh)
    print(data,type(data))
   # data.update(#give updated data)
#then just open file in write mode and dump the data