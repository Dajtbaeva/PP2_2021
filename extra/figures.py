from math import pi

class Figures:
    def __init__(self, color):
        self.color = color

class Krug(Figures):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2
    
    def get_dlina(self):
        return 2 * pi * self.radius

    def compare_areas(self, K):
        if self.get_area() > K.get_area():
            return self.get_area()
        else:
            return K.get_area() 

    # def get_info(self):
    #     return f'{self.manufacturer}, {self.color}, {self.year}'


class Square(Figures):
    def __init__(self, color, height):
        super().__init__(color)
        self.height = height

    def get_area(self):
        return self.height() ** 2

    def get_perimeter(self):
        return self.height() * 4

    def compare_perimeters(self, S):
        if self.get_perimeter() > S.get_perimeter():
            return self.get_perimeter()
        else:
            return S.get_perimeter()

def compare(C, S):
    if C.get_area() > S.get_area():
        return C.get_area()
    else:
        return S.get_area()

C1 = Krug("white", 5)
S1 = Square("red", 7)

print(C1.compare(S1))






    