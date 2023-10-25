class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other):
        if self.area() > other.area():
            return "This rectangle is larger."
        elif self.area() < other.area():
            return "This rectangle is smaller."
        else:
            return "Both rectangles have the same area."

rect1 = Rectangle(6, 7)
rect2 = Rectangle(6, 9)
print(rect1.compare_area(rect2))
