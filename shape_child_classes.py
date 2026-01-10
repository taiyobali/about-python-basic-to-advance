from item import Shape
import math
class Circle(Shape):
    def __init__(self,color:str,is_filled:bool,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def area(self):
        return f"Circle color is {self.color} and filled {self.is_filled}. area: {math.pi * self.radius} cm²"

class Triangle(Shape):
    def __init__(self, color: str, is_filled: bool, a:float, b:float, angle:float):
        super().__init__(color,is_filled)
        self.a = a
        self.b = b
        self.angle = angle

    def area(self):
        return f"Triangle color is {self.color} and filled {self.is_filled}. area;{0.5 * self.a * self.b * math.sin(self.angle)} cm²"

