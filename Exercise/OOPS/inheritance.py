class Vehicle:
    comapny_name="XYZ Company"
    def __init__(self,n_wheels,n_seats,mileage):
        self.n_wheels=n_wheels
        self.n_seats=n_seats
        self.mileage=mileage
    def get_details(self):
        return f"Wheels are {self.n_wheels} seats are {self.n_seats} mileage is {self.mileage}"
"""
v1=Vehicle(4,7,30)        
print(v1.get_details())
"""


class Car(Vehicle):
    model="ABC123"
    def __init__(self,car_type,drive_type,n_wheels,n_seats,mileage):
        self.car_type=car_type
        self.drive_type=drive_type
        super().__init__(n_wheels,n_seats,mileage)

c1=Car("Diesel","Manual",4,7,8)
print(c1.get_details())
print(c1.car_type,c1.drive_type)