# Instance Method
# methods defined inside a class which is bound to/ associated with the instance/ object
class Student:
    """
    This is a class student to manage student info and activities 
    """
    def study(self,hours):
        print(f"Self:{self}")
        print(f"Student studied for {hours} hours")
    def sports(self,sports):
        print(f"Student plays {sports}")
student1=Student()
print(f"Object:{student1}")
student1.study(2)
student1.sports("Cricket")
# object itself is passed as first as first argument   
print("-------------------------------------")
student2=Student()
print(f"Object:{student2}")
student2.study(5)
student2.sports("Basketball")