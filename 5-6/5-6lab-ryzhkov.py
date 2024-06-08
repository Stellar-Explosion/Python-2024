import math

# Класс Точка
class Point:
    def __init__(self, x, y, name):
        self.x = x  # координата x
        self.y = y  # координата y
        self.name = name  # имя точки
    
    def __str__(self):
        return f"{self.name}({self.x},{self.y})"  # строковое представление точки

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.name == other.name  # сравнение точек
        return False

    def __hash__(self):
        return hash((self.x, self.y, self.name))  # хэширование точки

    def __add__(self, other):
        if isinstance(other, Point):
            return Segment(self, other)  # сложение двух точек возвращает отрезок
        return NotImplemented
        
# Класс Отрезок
class Segment:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1  # первая точка отрезка
        self.point2 = point2  # вторая точка отрезка
        
    def get_len(self):
        return math.sqrt((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)  # длина отрезка

    def __str__(self):
        return f"{self.point1.name}{self.point2.name}({self.point1.x}, {self.point1.y}; {self.point2.x}, {self.point2.y})"  # строковое представление отрезка

    def __add__(self, other):
        if isinstance(other, Segment):
            points = [self.point1, self.point2, other.point1, other.point2]  # объединение точек двух отрезков
            return BrokenLine(points)  # сложение двух отрезков возвращает ломаную линию
        return NotImplemented
        
# Класс Ломаная Линия
class BrokenLine:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Надо не менее 3 точек")  # проверка на минимальное количество точек
        self.points = points  # список точек
        
    def get_len(self):
        total_length = 0
        for i in range(len(self.points) - 1):
            segment = Segment(self.points[i], self.points[i + 1])  # создание отрезка между двумя соседними точками
            total_length += segment.get_len()  # суммирование длин всех отрезков
        return total_length

    def __str__(self):
        return ','.join(point.name for point in self.points)  # строковое представление ломаной линии

    def __add__(self, other):
        if isinstance(other, Point):
            new_points = self.points + [other]  # добавление новой точки к ломаной линии
            return BrokenLine(new_points)  # возвращает новую ломаную линию
        return NotImplemented