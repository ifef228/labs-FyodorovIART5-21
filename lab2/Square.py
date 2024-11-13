from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a, color):
        super().__init__(a, a, color)
        self.title = 'Square'

    def __repr__(self):
        return f"""title: {self.title}; a = {self.a}; color(r, g, b):
         ({self.color.r}, {self.color.g}, {self.color.b}); square:{self.square()}"""
