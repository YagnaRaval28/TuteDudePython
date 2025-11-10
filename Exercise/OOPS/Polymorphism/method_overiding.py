class Employee:
    def working_hours(self):
        return 45
class Intern(Employee):
    def working_hours(self):
        return 40

obj=Intern()
print(obj.working_hours())