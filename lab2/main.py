from Circle import Circle
from Color import ShapeColor
from Rectangle import Rectangle
from Square import Square


def main():
    color = ShapeColor(1, 2, 3)
    rectangle = Rectangle(1, 2, color)
    circle = Circle(1, color)
    square = Square(1, color)

    print(rectangle.__repr__())
    print(circle.__repr__())
    print(square.__repr__())


if __name__ == '__main__':
    main()
