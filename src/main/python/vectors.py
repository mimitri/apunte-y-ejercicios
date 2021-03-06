class VectorND:

    def __init__(self, tail):
        self.tail = tail

    def add(self, other_vector):
        components = []
        if len(self.tail) > len(other_vector.tail):
            bigger = self.tail
            smaller = other_vector.tail
        else:
            bigger = other_vector.tail
            smaller = self.tail
        for i in range(0, len(smaller.tail)):
            components.append(bigger.tail[i] + smaller.tail[i])
        for i in range(len(smaller.tail), len(bigger.tail)):
            components.append(bigger.tail[i])
        return VectorND(components)

    def print(self):
        result = ""
        for idx in range(0, len(self.tail)):
            result += str(self.tail[idx])
            if idx < len(self.tail) - 1:
                result += ", "
        print(f"({result})")


class Vector2D(VectorND):

    def __init__(self, x, y):
        super().__init__([x, y])
