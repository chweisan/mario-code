import pyxel

from constants import SPRITE_SPEED_X
from constants import GRAVITY
from constants import SPRITE_JUMP_INITIAL_SPEED

class Mario:
    def __init__(self, x: int, y: int, size: int):
        """
        :param x: int,
        :param y: int,
        :param size: int
        """
        # position in the sprite image bank: image, u (x posit in bank),
        # v (y image posit in bank), w, h
        self.sprite = [0, 0, 0, 16, 24]
        self.mario_w = self.sprite[3]  # height
        self.__dying = False
        self.jumping = False
        self.gravity = GRAVITY
        self.__x = x
        self.__y = y
        self.x_vel = SPRITE_SPEED_X
        self.y_vel = 0
        self.size = size
        self.fall_count = 0
        self.image = 0  # base image
        # lives: at some point he can have four I believe we can make it so
        # that for every level he passes he can gain one life up to 4
        self.__lives = 3

    def move_y(self, dy):
        self.y -= dy

    def move_x(self, direc: bool):
        if direc:  # and self.x < (self.size + 1):
            self.sprite[3] = 16
            self.x += self.x_vel
        elif not direc:  # and self.x > (-1 - self.__mario_size):
            # because size starts counting in the upper left corner
            self.sprite[3] = -16
            self.x -= self.x_vel
        if self.x >= (self.size + 1):
            self.x = 0 - self.mario_w
        elif self.x <= (-1 - self.mario_w):
            self.x = self.size

    def loop(self):
        self.y_vel -= self.gravity
        self.move_y(self.y_vel)
        self.fall_count += 8

    def jump(self):
        self.fall_count = 0
        self.y_vel = SPRITE_JUMP_INITIAL_SPEED

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            self.__x = x

    @property
    def y(self) -> int:
        return int(self.__y)

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def lives(self) -> int:
        return self.__lives

    @lives.setter
    def lives(self, lives: int):
        if type(lives) is not int:
            raise TypeError("lives value must be an integer")
        elif lives > 3:
            raise ValueError("Mario can't have more than 3 lives")
        else:
            self.__lives = lives

    @property
    def dying(self) -> bool:
        return self.__dying

    @dying.setter
    def dying(self, new_dying):
        self.__dying = new_dying

    def draw(self):
        if not self.__dying:
            pyxel.blt(self.__x, self.__y, *self.sprite, colkey=0)



    # terreno: organizar por listas
    # position change doesn't have to be inside the same if of jumping??
    # define touch another object so it stops???
