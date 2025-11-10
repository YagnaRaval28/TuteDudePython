class SalaryError(Exception):
    pass
def check_salary(salary):
    if salary<0:
        raise SalaryError("Salary Cannot be less than zero")
    else:
        print("Salary:",salary)
sal=int(input("Enter Salary:"))
print(check_salary(sal))