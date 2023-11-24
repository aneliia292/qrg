from dataclasses import dataclass

class Money:

    def __init__(self, rubles, kopecks): #сохраняем обьекты в класс
        self.rubles = rubles
        self.kopecks = kopecks

    def __add__(self, other): #метод для операций сложения
        total_kopecks = self.kopecks + other.kopecks
        carry_over = total_kopecks // 100
        total_kopecks = total_kopecks % 100
        total_rubles = self.rubles + other.rubles + carry_over
        return Money(total_rubles, total_kopecks)

    def __sub__(self, other): #метод для вычитания обьектов
        total_kopecks = self.kopecks - other.kopecks
        if total_kopecks < 0:
            total_kopecks += 100
            total_rubles = self.rubles - other.rubles - 1
        else:
            total_rubles = self.rubles - other.rubles
            return Money(total_rubles, total_kopecks)

    def __truediv__(self, divisor): #делит обьекты
        total_kopecks = self.rubles * 100 + self.kopecks
        total_kopecks /= divisor
        total_rubles = int(total_kopecks // 100)
        total_kopecks = int(total_kopecks % 100)
        return Money(total_rubles, total_kopecks)

    def __mul__(self, multiplier): #метод умножения
        total_kopecks = self.rubles * 100 + self.kopecks
        total_kopecks *= multiplier
        total_rubles = int(total_kopecks // 100)
        total_kopecks = int(total_kopecks % 100)
        return Money(total_rubles, total_kopecks)

    def __eq__(self, other): #сравнивает обьекты
        return (self.rubles, self.kopecks) == (other.rubles, other.kopecks)

    def __lt__(self, other): #сравнивает меньшие обьекты
        return (self.rubles, self.kopecks) < (other.rubles, other.kopecks)

    def __str__(self): #разделяет дробную часть запятой
        return f"{self.rubles},{self.kopecks:02d}"

money1 = Money(10, 50)
money2 = Money(5, 70)

print(money1 + money2)  #Сложение
print(money1 - money2)  #Вычитание
print(money1 / 3)  #Деление на число
print(money1 * 2.5)  #Умножение на число
print(money1 == money2)  #Сравнение на равенство
print(money1 < money2)  #Сравнение на меньше