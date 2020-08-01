class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        s = 3 * 3 ** 0.5 * self.side_length ** 2 / 2
        return '%.3f' % s
