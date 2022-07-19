from designpattern.creational_patterns.shape import *


class ShapeFactory:
    def get_shape(self, shape_type=None) -> Shape:
        if not shape_type:
            return

        if shape_type == "Circle":
            return Circle()

        if shape_type == "Square":
            return Square()

        if shape_type == "Rectangle":
            return Rectangle()

        return


if __name__ == '__main__':
    factory = ShapeFactory()
    circle = factory.get_shape('Circle')
    print(isinstance(circle, Circle))

    square = factory.get_shape('Square')
    print(isinstance(square, Square))

    rectangle = factory.get_shape('Rectangle')
    print(isinstance(rectangle, Rectangle))
