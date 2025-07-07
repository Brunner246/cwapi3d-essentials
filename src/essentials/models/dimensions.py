import dataclasses


@dataclasses.dataclass
class Dimensions:
    length: float = 1_000.0
    width: float = 120.0
    height: float = 240.0

    def __post_init__(self):
        if not isinstance(self.length, (int, float)):
            raise TypeError("length must be a number")
        if not isinstance(self.width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(self.height, (int, float)):
            raise TypeError("height must be a number")

        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError("Dimensions must be positive numbers")
