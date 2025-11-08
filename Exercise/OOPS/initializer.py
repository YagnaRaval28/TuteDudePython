#__init__() method
# is an instance method
# is used to create and initialize the attributes during the object creation
class Student:
    """
    This is a class student to manage student info and activities 
    """
    def __init__(self,n,roll):
        self.name=n
        self.roll=roll
    def study(self,hours):
        print(f"Self:{self}")
        print(f"Student studied for {hours} hours")
    def sports(self,sports):
        print(f"Student plays {sports}")

student1=Student("John",101) 
student2=Student("Carol",102)
print(student1.name,student1.roll)       
print(student2.name,student2.roll)