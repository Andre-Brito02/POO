import math

class Rectangle:
    def __init__(self, width:float, height:float):
        self._width = width
        self._height = height

    def area_rectangle(self):
        return self._width*self._height

    def perimeter_rectangle(self):
        return 2*(self._width+self._height)

    def diagonal_rectangle(self):
        return math.sqrt(math.pow(self._width, 2) + math.pow(self._height, 2))

    def __str__(self):
        return f"AREA = {self.area_rectangle():.2f}\nPERIMETER = {self.perimeter_rectangle():.2f}\nDIAGONAL = {self.diagonal_rectangle():.2f}"

print("Enter rectangle width and height: ")
width = float(input("Width: "))
height = float(input("Height: "))
rec = Rectangle(width, height)
print(rec)