from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius})"


# Vector operations
v1 = Vector(3, 4)
v2 = Vector(2, 1)

print("VECTOR OPERATIONS")
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", v1 + v2)
print("Magnitude of Vector 1:", round(v1.magnitude(), 2))
print("Vector 1 < Vector 2:", v1 < v2)
print("Vector 1 == Vector 2:", v1 == v2)

# Abstract shape implementation
circle = Circle(5)

print("\nABSTRACT SHAPE")
print("Shape:", circle)
print("Circle Area:", round(circle.area(), 2))
