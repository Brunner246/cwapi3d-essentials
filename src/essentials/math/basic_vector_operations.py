import math


class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """Vector addition"""
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Vector subtraction"""
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """Scalar multiplication"""
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        """Scalar division"""
        if scalar == 0:
            raise ValueError("Division by zero")
        return Point3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def magnitude(self):
        """Calculate vector magnitude/length"""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Point3D(0, 0, 0)
        return self / mag

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        """Cross product"""
        return Point3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def distance_to(self, other):
        """Distance between two points"""
        return (self - other).magnitude()
