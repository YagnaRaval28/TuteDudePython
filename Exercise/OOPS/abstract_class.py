from my_abstract_class import Shape
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2    
    
class Recatngle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width        

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2     
sq1=Square(10)
print(sq1.area())

r1=Recatngle(10,5)
print(r1.area())

c1=Circle(10)
print(c1.area())

#Abstarct class is a template or framework to create classes