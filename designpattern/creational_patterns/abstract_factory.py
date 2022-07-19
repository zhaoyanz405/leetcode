from designpattern.creational_patterns.color import Red, Green, Blue
from designpattern.creational_patterns.shape import Circle, Rectangle, Square


class AbstractFactory:
    def get_color(self, color):
        raise NotImplemented

    def get_shape(self, shape):
        raise NotImplemented


class ShapeFactory(AbstractFactory):
    def get_shape(self, shape):
        if not shape:
            return

        if shape == "Circle":
            return Circle()

        if shape == "Rectangle":
            return Rectangle()

        if shape == "Square":
            return Square()

        return

    def get_color(self, color):
        return


class ColorFactory(AbstractFactory):
    def get_shape(self, shape):
        return

    def get_color(self, color):
        if color == "Red":
            return Red()

        if color == "Green":
            return Green()

        if color == "Blue":
            return Blue()

        return


class FactoryProducer:

    @staticmethod
    def get_factory(choice):
        if choice == "shape":
            return ShapeFactory()
        if choice == "color":
            return ColorFactory()

        return


if __name__ == '__main__':
    shape_factory = FactoryProducer.get_factory("shape")
    circle = shape_factory.get_shape("Circle")
    assert isinstance(circle, Circle)

    square = shape_factory.get_shape("Square")
    assert isinstance(square, Square)

    color_factory = FactoryProducer.get_factory("color")
    red = color_factory.get_color("Red")
    assert isinstance(red, Red)

    blue = color_factory.get_color("Blue")
    assert isinstance(blue, Blue)
