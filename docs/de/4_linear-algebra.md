# 3D Vector Mathematics for cadwork API

This repository contains essential 3D vector mathematics functions for working with cadwork's 3D geometry system. The
functions demonstrate fundamental linear algebra operations on vectors and points in 3D space.

## Vector vs Point Distinction

Understanding the difference between **vectors** and **points** is crucial for 3D geometry:

### Points (Absolute Positions)

- Represent **fixed locations** in 3D space
- Have absolute coordinates: P = (x, y, z)
- Examples: cadwork element points P1, P2, P3
- Operations: translation, but not scaling

### Vectors (Direction & Magnitude)

- Represent **direction and distance** in space
- Relative displacement: V = (x, y, z)
- Examples: normal vectors, movement directions
- Operations: addition, subtraction, scaling, normalization

## Core Vector Operations

### Basic Arithmetic Operations

#### Vector Addition

```python
def vector_add(p1, p2):
    """Add two vectors - combines their directional components"""
    result_x = p1.x + p2.x
    result_y = p1.y + p2.y
    result_z = p1.z + p2.z
    return Point3D(result_x, result_y, result_z)
```

**Linear Algebra**: `v₁ + v₂ = (x₁+x₂, y₁+y₂, z₁+z₂)`

- Combines two displacement vectors
- Follows parallelogram rule
- Commutative: `v₁ + v₂ = v₂ + v₁`

#### Vector Subtraction

```python
def vector_subtract(p1, p2):
    """Subtract vector p2 from p1 - finds displacement between vectors"""
    result_x = p1.x - p2.x
    result_y = p1.y - p2.y
    result_z = p1.z - p2.z
    return Point3D(result_x, result_y, result_z)
```

**Linear Algebra**: `v₁ - v₂ = (x₁-x₂, y₁-y₂, z₁-z₂)`

- Finds the vector from p2 to p1
- When subtracting points: gives displacement vector
- Non-commutative: `v₁ - v₂ ≠ v₂ - v₁`

#### Scalar Multiplication

```python
def vector_multiply_scalar(p, scalar):
    """Multiply vector by scalar - scales magnitude while preserving direction"""
    result_x = p.x * scalar
    result_y = p.y * scalar
    result_z = p.z * scalar
    return Point3D(result_x, result_y, result_z)
```

**Linear Algebra**: `k·v = (k·x, k·y, k·z)`

- Scales vector magnitude by factor k
- Preserves direction (if k > 0) or reverses it (if k < 0)
- Essential for unit vector creation and resizing

### Magnitude and Normalization

#### Vector Magnitude (Length)

```python
def vector_magnitude(p):
    """Calculate vector magnitude using Euclidean norm"""
    x_squared = p.x * p.x
    y_squared = p.y * p.y
    z_squared = p.z * p.z
    magnitude = math.sqrt(x_squared + y_squared + z_squared)
    return magnitude
```

**Linear Algebra**: `|v| = √(x² + y² + z²)`

- Euclidean distance from origin
- Always non-negative
- Zero only for zero vector

#### Vector Normalization

```python
def vector_normalize(p):
    """Normalize vector to unit length while preserving direction"""
    mag = vector_magnitude(p)
    if mag == 0:
        return Point3D(0, 0, 0)
    norm_x = p.x / mag
    norm_y = p.y / mag
    norm_z = p.z / mag
    return Point3D(norm_x, norm_y, norm_z)
```

**Linear Algebra**: `v̂ = v/|v|` where `|v̂| = 1`

- Creates unit vector (magnitude = 1)
- Preserves direction
- Critical for direction-only calculations

### Advanced Vector Operations

#### Dot Product (Scalar Product)

```python
def vector_dot_product(p1, p2):
    """Calculate dot product - measures vector alignment"""
    dot_x = p1.x * p2.x
    dot_y = p1.y * p2.y
    dot_z = p1.z * p2.z
    dot_result = dot_x + dot_y + dot_z
    return dot_result
```

**Linear Algebra**: `v₁ · v₂ = x₁x₂ + y₁y₂ + z₁z₂ = |v₁||v₂|cos(θ)`

- Returns scalar value
- Measures how "aligned" vectors are
- Zero for perpendicular vectors
- Applications: projection, angle calculation

#### Cross Product (Vector Product)

```python
def vector_cross_product(p1, p2):
    """Calculate cross product - finds perpendicular vector"""
    cross_x = p1.y * p2.z - p1.z * p2.y
    cross_y = p1.z * p2.x - p1.x * p2.z
    cross_z = p1.x * p2.y - p1.y * p2.x
    return Point3D(cross_x, cross_y, cross_z)
```

**Linear Algebra**: `v₁ × v₂ = (y₁z₂-z₁y₂, z₁x₂-x₁z₂, x₁y₂-y₁x₂)`

- Returns vector perpendicular to both inputs
- Magnitude = area of parallelogram formed by vectors
- Direction follows right-hand rule
- Zero for parallel vectors

### Distance and Angle Calculations

#### Distance Between Points

```python
def vector_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    diff_x = p1.x - p2.x
    diff_y = p1.y - p2.y
    diff_z = p1.z - p2.z
    distance = math.sqrt(diff_x * diff_x + diff_y * diff_y + diff_z * diff_z)
    return distance
```

**Linear Algebra**: `d = |p₁ - p₂| = √[(x₁-x₂)² + (y₁-y₂)² + (z₁-z₂)²]`

- Euclidean distance in 3D space
- Always non-negative
- Symmetric: `d(p₁,p₂) = d(p₂,p₁)`

