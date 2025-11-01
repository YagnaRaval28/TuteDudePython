# Local variable - created within a function
# Global variable - created outside all the functions
age = 25
def age_func():
    global age
    age=age+2
    print(f"Inside function {age}")


age_func()
print(f"Outside function {age}")