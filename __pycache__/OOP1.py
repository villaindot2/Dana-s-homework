import re
import turtle

#1) Solve using OOP / Make a Circle with OOP (20)


class Circle:
    def __init__(self, radius=20):
        self.radius = radius
    def get_area(self):
        window = turtle.Screen()
        turtle.shape("turtle")
        window.title("Circle")
        turtle.circle(self.radius)    
        window.exitonclick()


obj = Circle()  
print(obj.get_area())