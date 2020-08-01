class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = 0.5 * self.a * self.b if self.c ** 2 == self.a ** 2 + self.b ** 2 else "Not right"


input_c, input_a, input_b = [int(x) for x in input().split()]

print(RightTriangle(input_c, input_a, input_b).area)
