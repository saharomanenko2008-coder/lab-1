import math
class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
        elif a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p=self.perimeter()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Rectangle:
    def __init__(self, a, b):
        if a <= 0 or b <= 0 :
            raise ValueError
        else:
            self.a = a
            self.b = b
    def perimeter(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.b

class Trapeze:
    def __init__(self, a, b, c,d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError
        else:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        x = abs(self.a - self.b)
        if x == 0:
            return 0
        h = math.sqrt(max(0, self.c ** 2 - (((x ** 2 + self.c ** 2 - self.d ** 2) / (2 * x)) ** 2)))
        return ((self.a + self.b) / 2) * h


class Parallelogram:
    def __init__(self, a, b, h):
        if a <= 0 or b <= 0 or h <= 0 or h > a or h > b:
            raise ValueError
        else:
            self.a = a
            self.b = b
            self.h = h
    def perimeter(self):
        return 2*(self.a + self.b)
    def area(self):
        return self.a*self.h

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError
        else:
            self.radius = radius
    def perimeter(self):
        return 2*math.pi*self.radius
    def area(self):
        return math.pi*self.radius**2


if __name__ == '__main__':
    all_figures = []
    file = input("Enter the file name: ")

    with open(file, "r") as f:
        for line in f:
            el = line.split()
            if not el: continue

            name = el[0]
            args = [float(x) for x in el[1:]]

            try:
                classes = {"Triangle": Triangle, "Rectangle": Rectangle,
                           "Trapeze": Trapeze, "Parallelogram": Parallelogram, "Circle": Circle}
                if name in classes:
                    all_figures.append(classes[name](*args))
            except ValueError:
                continue

    if all_figures:
        max_area = max(all_figures, key=lambda f: f.area())
        max_perimetr = max(all_figures, key=lambda f: f.perimeter())

        print(f"Max Area: {type(max_area).__name__} ({max_area.area():.2f})")
        print(f"Max Perimeter: {type(max_perimetr).__name__} ({max_perimetr.perimeter():.2f})")
