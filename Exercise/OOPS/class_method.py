# Class methods are methods defined inside the class that are bound to the class
# To create a class method we use decorator -> classmethod
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
    @classmethod
    def greet(cls):
        print(f"Welcome to the {cls.college_name}")  
    @classmethod
    def departments(cls):
        print(f"The departments in {cls.college_name} are:")
        for dep in cls.department:
            print(dep)      
student1=Student("John",101)   
student1.greet()
student1.departments()   
