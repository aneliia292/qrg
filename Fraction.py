from dataclasses import dataclass
class Fraction:

    def __init__(self, whole_part, fractional_part):
        self.whole_part = whole_part #Целая часть длинное целое со знаком
        self.fractional_part = fractional_part #Дробная часть беззнаковое короткое целое

    def __add__(self, other): #метод add складывает
        new_whole_part = self.whole_part + other.whole_part
        new_fractional_part = self.fractional_part + other.fractional_part
        if new_fractional_part >= 1: #Проверяем не превышена ли единица
            new_whole_part += 1
            new_fractional_part -= 1
        return Fraction(new_whole_part, new_fractional_part)

    def __sub__(self, other): #метод sub вычитает
        new_whole_part = self.whole_part - other.whole_part
        new_fractional_part = self.fractional_part - other.fractional_part
        if new_fractional_part < 0:
            new_whole_part -= 1
            new_fractional_part += 1
        return Fraction(new_whole_part, new_fractional_part)

    def __mul__(self, other): #метод mul отвечает за умножение
        new_whole_part = self.whole_part * other.whole_part
        new_fractional_part = self.fractional_part * other.fractional_part
        return Fraction(new_whole_part, new_fractional_part)

    def __eq__(self, other): #метод eq сравнивает обьекты класса
        return (self.whole_part, self.fractional_part) == (other.whole_part, other.fractional_part)


        fraction1 = Fraction(3, 4)
        fraction2 = Fraction(1, 2)

        #арифметические операции со значениями класса
        sum_result = fraction1 + fraction2
        diff_result = fraction1 - fraction2
        mul_result = fraction1 * fraction2

        print(sum_result.whole_part, sum_result.fractional_part)
        print(diff_result.whole_part, diff_result.fractional_part)
        print(mul_result.whole_part, mul_result.fractional_part)
        print(fraction1 == fraction2)