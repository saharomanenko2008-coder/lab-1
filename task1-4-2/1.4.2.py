import math


class Polygon:
    def __init__(self, name, coords):
        self.name = name
        self.vertices = []
        for i in range(0, len(coords), 2):
            self.vertices.append((float(coords[i]), float(coords[i + 1])))

    def get_dim(self):
        return len(self.vertices)

    def is_convex(self):
        n = len(self.vertices)
        if n < 3:
            return False

        def cross_product(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        signs = []
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % n]
            p3 = self.vertices[(i + 2) % n]
            cp = cross_product(p1, p2, p3)
            if cp != 0:
                signs.append(cp > 0)

        return all(s == signs[0] for s in signs)

    def output(self):
        print(f"{self.name} (вершин: {self.get_dim()}): {self.vertices}")


class Pentagon(Polygon):
    def __init__(self, coords):
        super().__init__("Pentagon", coords)


class Hexagon(Polygon):
    def __init__(self, coords):
        super().__init__("Hexagon", coords)


if __name__ == "__main__":
    file = "input"
    all_polygons = []


    with open(file, "r") as f:
        for line in f:
            parts = line.split()
            if not parts: continue

            name = parts[0].lower()
            coords = parts[1:]

            if name == "pentagon":
                all_polygons.append(Pentagon(coords))
            elif name == "hexagon":
                all_polygons.append(Hexagon(coords))
            else:
                all_polygons.append(Polygon("Polygon", coords))

    convex_count = 0
    for p in all_polygons:
        if p.is_convex():
            p.output()
            convex_count += 1

    if convex_count == 0:
        print("Опуклих фігур не знайдено.")
