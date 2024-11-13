import math

from Color import ShapeColor
from Shape import Shape


class Circle(Shape):
    def __init__(self, r, color):
        self.r = r
        self.color = ShapeColor(color.r, color.g, color.b)
        self.title = 'Circle'

    def square(self):
        return math.pi * self.r ** 2

    def __repr__(self):
        return f"""title: {self.title}; r = {self.r}; color(r, g, b):
         ({self.color.r}, {self.color.g}, {self.color.b}); square:{self.square()}"""