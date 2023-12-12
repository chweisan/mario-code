from entities import Entities


class Coin(Entities):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.sprite = [0, 16, 104, 0, 8]
        self.width = 8
        self.__animation = None