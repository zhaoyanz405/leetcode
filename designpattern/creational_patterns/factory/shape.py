class Shape:
    def draw(self):
        raise NotImplemented


class Circle(Shape):
    def draw(self):
        print("draw circle")


class Square(Shape):
    def draw(self):
        print("draw Square")


class Rectangle(Shape):
    def draw(self):
        print("draw Rectangle")
