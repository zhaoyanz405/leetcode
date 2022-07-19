class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("draw circle")


class Square(Shape):
    def draw(self):
        print("draw Square")


class Rectangle(Shape):
    def draw(self):
        print("draw Rectangle")


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
