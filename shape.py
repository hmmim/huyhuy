import math


class shape:
    pass


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.radius * 2
        self.perimeter = None
        self.acreage = None

    def calculate_perimeter_circle(self):
        self.perimeter = self.radius * math.pi
        return self.perimeter;

    def calculate_acreage_circle(self):
        self.acreage = self.radius * self.radius * math.pi
        return self.acreage;


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter_rectangle(self):
        self.perimeter = (self.length + self.width) * 2
        return self.perimeter;

    def calculate_acreage_rectangle(self):
        self.acreage = self.length * self.width
        return self.acreage;


class Triangle:
    def __init__(self, edge_1, edge_2, edge_3):
        self.edge_1 = edge_1
        self.edge_2 = edge_2
        self.edge_3 = edge_3

    def calculate_perimeter_triangle(self):
        self.perimeter = (self.edge_1 + self.edge_2 + self.edge_3)
        return self.perimeter;

    def calculate_acreage_triangle(self):
        p = (self.edge_1 + self.edge_2 + self.edge_3) / 2
        self.acreage = math.sqrt((p - self.edge_1) * (p - self.edge_2) * (p - self.edge_3))
        return self.acreage;


circle = Circle(5)
print("Circle - Radius:", circle.radius)
print("Circle - Perimeter:", round(circle.calculate_perimeter_circle(),2))
print("Circle - Area:", round(circle.calculate_acreage_circle(),2))
rectangle = Rectangle(4, 6)
print("\nRectangle - Length:", rectangle.length)
print("Rectangle - Width:", rectangle.width)
print("Rectangle - Perimeter:", rectangle.calculate_perimeter_rectangle())
print("Rectangle - Area:", rectangle.calculate_acreage_rectangle())
triangle = Triangle(3, 4, 5)
print("\nTriangle - Edge 1:", triangle.edge_1)
print("Triangle - Edge 2:", triangle.edge_2)
print("Triangle - Edge 3:", triangle.edge_3)
print("Triangle - Perimeter:", triangle.calculate_perimeter_triangle())
print("Triangle - Area:", round(triangle.calculate_acreage_triangle(),2))
