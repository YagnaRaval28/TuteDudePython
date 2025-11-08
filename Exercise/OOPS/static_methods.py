"""
static method- method defined inside a class which is neither bound to object nor to class

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
    @staticmethod
    def greet():
        print(f"Welcome to the College")  
    @classmethod
    def departments(cls):
        print(f"The departments in {cls.college_name} are:")
        for dep in cls.department:
            print(dep)      
student1=Student("John",101)   
student1.greet()
student1.departments()   
