from designpattern.creational_patterns.shape import Circle, Rectangle, Square


class Color:
    def fill(self):
        raise NotImplemented


class Red(Color):
    def fill(self):
        print("fill red")


class Green(Color):
    def fill(self):
        print("fill Green")


class Blue(Color):
    def fill(self):
        print("fill Blue")
