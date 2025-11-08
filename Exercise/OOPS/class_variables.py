"""
Class variables are defined at the class level
Same copy of the class variables are shared among the objects
"""
class Student:
    """
    This is a class student to manage student info and activities 
    """
    college_name="FET"
    department=['CSE','MCA','MSCIT']
    def __init__(self,n,roll):
        self.name=n
        self.roll=roll
    def study(self,hours):
        print(f"Self:{self}")
        print(f"Student studied for {hours} hours")
    def sports(self,sports):
        print(f"Student plays {sports}")
student1=Student("John",101)    
print(student1.college_name)
print(student1.department)    
help(Student)