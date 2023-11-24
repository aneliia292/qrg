import math

class Trapezoid:

    def __init__(self, coordinates): #охраняем обьекты в класс
        self.coordinates = coordinates

    def is_isosceles(self):
        ab = self._distance(self.coordinates[0], self.coordinates[1])
        bc = self._distance(self.coordinates[1], self.coordinates[2])
        cd = self._distance(self.coordinates[2], self.coordinates[3])
        da = self._distance(self.coordinates[3], self.coordinates[0])
        if ab == cd and bc != da:
            return True
        elif bc == da and ab != cd:
            return True
        else:
            return False

    def side_lengths(self): #длина сторон
        ab = self._distance(self.coordinates[0], self.coordinates[1])
        bc = self._distance(self.coordinates[1], self.coordinates[2])
        cd = self._distance(self.coordinates[2], self.coordinates[3])
        da = self._distance(self.coordinates[3], self.coordinates[0])
        return ab, bc, cd, da

    def perimeter(self): #сохранение формулы для вычисления периметра
        ab, bc, cd, da = self.side_lengths()
        return ab + bc + cd + da

    def area(self): #вычисление площади
        ab, bc, cd, da = self.side_lengths()
        h = self._height(ab, bc, cd, da)
        return 0.5 * (ab + cd) * h

    def _distance(self, point1, point2): #расстояние между точками
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

    def _height(self, ab, bc, cd, da): #вычисление высоты
        return math.sqrt(ab**2 - 0.25*((bc - da)**2 + ab**2 - cd**2 )**2 / (bc - da)**2 )


trapezoid1 = Trapezoid([(0, 0), (4, 3), (8, 3), (12, 0)])
trapezoid2 = Trapezoid([(0, 0), (3, 4), (3, 8), (0, 12)])

print(trapezoid1.is_isosceles()) #Проверка на равнобедренность
print(trapezoid1.side_lengths()) #Длины сторон
print(trapezoid1.perimeter()) #Периметр
print(trapezoid1.area()) #Площадь