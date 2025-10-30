# *args= variable legth positional arguments (0 to n)
# we can use any variable name instead of args
# *args is a standard
""" 
def add(*nums):
    print(sum(nums))
add(10,20)    """
"""
def student_info(sid,sname,*marks):
    percent=sum(marks)/len(marks)
    print(f"{sname} with {sid} got {percent}%")
name=input("Enter your name:")
id=input("Enter your id:")
student_info(id,name,85,75,77,89)    

"""

#**kwargs- variable length keyword arguments
def student_info(sid,sname,**marks):
    percent=sum(marks.values())/len(marks)
    print(f"{sname} with id {sid} got {percent}%")
student_info(101,"Yagna",English=86,Maths=90,Science=85)  