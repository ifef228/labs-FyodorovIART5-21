from Color import ShapeColor
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = ShapeColor(color.r, color.g, color.b)
        self.title = 'Rectangle'

    def square(self):
        return self.a * self.b

    def __repr__(self):
        return f"""title: {self.title}; (a,b): ({self.a}, {self.b}); color(r, g, b):
         ({self.color.r}, {self.color.g}, {self.color.b}); square:{self.square()}"""
