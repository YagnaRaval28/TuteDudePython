student={'John':95,'Mark':85}
name=input("Enter the student's name:")
if name in student:
    print(f"{name}'s marks:{student[name]}")
else:
    print("Student not found")    