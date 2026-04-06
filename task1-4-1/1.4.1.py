import math

class Vector:
    def __init__(self, coords):
        if isinstance(coords, Vector):
            self.coords = list(coords.coords)
        else:
            self.coords = [float(x) for x in coords]

    def output(self):
        print("вектор: (", end="")
        print(*self.coords, sep=", ", end=")\n")

    def dim(self):
        return len(self.coords)

    def length(self):
        sum_sq = sum(x ** 2 for x in self.coords)
        return math.sqrt(sum_sq)

    def av_coords(self):
        return sum(self.coords) / len(self.coords)

    def min_coords(self):
        return min(self.coords)

    def max_coords(self):
        return max(self.coords)

if __name__ == '__main__':
    file = input("Введіть ім'я файла: ")
    all_vectors= []

    with open(file ,"r") as f:
        for line in f:
            parts = line.split()
            if parts:
                v = Vector(parts)
                all_vectors.append(v)


    if all_vectors:
        vl_dim = all_vectors[0]

        for v in all_vectors[1:]:
            if v.dim() > vl_dim.dim():
                vl_dim = v

            elif v.dim() == vl_dim.dim():
                if v.length() < vl_dim.length():
                    vl_dim = v

        print("Вектор з найбільшою розмірністю - це", end=" ")
        vl_dim.output()


        vl_len = all_vectors[0]
        for v in all_vectors[1:]:
            if v.length() > vl_len.length():
                vl_len = v
            elif v.length() == vl_len.length():
                if v.dim()<vl_len.dim():
                    vl_len = v

        print("Вектор з найбільшою довжиною - це", end=" ")
        vl_len.output()


        sum_v_len = 0
        for v in all_vectors:
            sum_v_len+=v.length()
        average_v = sum_v_len/len(all_vectors)

        print(f"Середня довжина вектора - {average_v}")


        above_av_v= []
        for v in all_vectors:
            if v.length() > average_v:
                above_av_v.append(v)

        print(f"Кількість векторів довші за середнє значення: {len(above_av_v)}")


        max_coords_v = all_vectors[0]
        for v in all_vectors[1:]:
            if v.max_coords() > max_coords_v.max_coords():
                max_coords_v = v
            elif v.max_coords() == max_coords_v.max_coords():
                if v.min_coords()<max_coords_v.min_coords():
                    max_coords_v = v

        print(f"Вектор з найбільшою координатою - це ", end="")
        max_coords_v.output()


        min_coords_v = all_vectors[0]
        for v in all_vectors[1:]:
            if v.min_coords() < min_coords_v.min_coords():
                min_coords_v = v
            elif v.min_coords() == min_coords_v.min_coords():
                if v.max_coords() > min_coords_v.max_coords():
                    min_coords_v = v

        print(f"Вектор з найменшою координатою - це ", end="")
        min_coords_v.output()
