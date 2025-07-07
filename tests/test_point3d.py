import math

from essentials.math.basic_vector_operations import Point3D


def test_addition_of_two_points():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, 5, 6)
    result = p1 + p2
    assert result.x == 5, "X coordinate mismatch"
    assert result.y == 7, "Y coordinate mismatch"
    assert result.z == 9, "Z coordinate mismatch"


def test_subtraction_of_two_points():
    p1 = Point3D(4, 5, 6)
    p2 = Point3D(1, 2, 3)
    result = p1 - p2
    assert result.x == 3
    assert result.y == 3
    assert result.z == 3


def test_scalar_multiplication_of_point():
    p = Point3D(1, 2, 3)
    result = p * 2
    assert result.x == 2
    assert result.y == 4
    assert result.z == 6


def test_scalar_division_of_point():
    p = Point3D(2, 4, 6)
    result = p / 2
    assert math.isclose(result.x, 1)
    assert math.isclose(result.y, 2)
    assert math.isclose(result.z, 3)


def test_division_by_zero_raises_error():
    p = Point3D(1, 2, 3)
    try:
        p / 0
    except ValueError as e:
        assert str(e) == "Division by zero"


def test_magnitude_of_point():
    p = Point3D(3, 4, 0)
    result = p.magnitude()
    assert result == 5


def test_normalization_of_point():
    p = Point3D(3, 4, 0)
    result = p.normalize()
    assert result.x == 0.6
    assert result.y == 0.8
    assert result.z == 0


def test_normalization_of_zero_vector():
    p = Point3D(0, 0, 0)
    result = p.normalize()
    assert result.x == 0
    assert result.y == 0
    assert result.z == 0


def test_dot_product_of_two_points():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, -5, 6)
    result = p1.dot(p2)
    assert result == 12


def test_cross_product_of_two_points():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, 5, 6)
    result = p1.cross(p2)
    assert result.x == -3
    assert result.y == 6
    assert result.z == -3


def test_distance_between_two_points():
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, 5, 6)
    result = p1.distance_to(p2)
    assert result == math.sqrt(27)