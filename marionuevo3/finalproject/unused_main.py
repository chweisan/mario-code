import pyxel
from constants import WIDTH
from constants import HEIGHT
from constants import CAPTION
from tilemap import Tilemap


class Tile:
    # Creating this class to have in the same place the different values for
    # the positions of the objects on the background
    def __init__(self, u_mask: int, v_mask: int, img: int, w_mask: int,
                 h_mask: int):
        """ This function is used to initialize all the variables that are
        important in order to place elements
        :param u_mask: for value u
        :param v_mask: for value v
        :param img: the image used
        :param w_mask: for value w
        :param h_mask: for value h
        """
        self.__u_mask = u_mask
        self.__v_mask = v_mask
        self.__img = img
        self.__w_mask = w_mask
        self.__h_mask = h_mask

    @property
    # Only doing properties for the elements because once I give them
    # values, I don't want these values to change
    def u_mask(self) -> int:
        return self.__u_mask

    @property
    # Only doing properties for the elements because once I give them
    # values, I don't want these values to change
    def v_mask(self) -> int:
        return self.__v_mask

    @property
    # Only doing properties for the elements because once I give them
    # values, I don't want these values to change
    def img(self) -> int:
        return self.__img

    @property
    # Only doing properties for the elements because once I give them
    # values, I don't want these values to change
    def w_mask(self) -> int:
        return self.__w_mask

    @property
    # Only doing properties for the elements because once I give them
    # values, I don't want these values to change
    def h_mask(self) -> int:
        return self.__h_mask

    def draw(self, x: int, y: int):
        """Function to put the position of the image chosen
        :param x: for x-axis
        :param y: for y-axis
        """
        pyxel.blt(x, y, self.img,
                  self.u_mask, self.v_mask,
                  self.w_mask, self.h_mask)


class Layout:
    def __init__(self):
        self.__floor = Tile(0, 128, 0, 16, 16)
        self.__platform = Tile(16, 136, 0, 8, 8)

    def draw_floor(self):
        pos_bricks = 0
        for a in range(0, 16):
            self.floor.draw((0 + pos_bricks), 240)
            pos_bricks += self.floor.w_mask

    @property
    def floor(self) -> Tile:
        return self.__floor

    def draw_platform(self):
        pos_platform = 0
        for a in range(0, 12):
            self.platform.draw((0 + pos_platform), 200)
            pos_platform += 8

    @property
    def platform(self) -> Tile:
        return self.__platform


def update():
    """Function that must be in the program for pyxel to work"""
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()


def draw():
    """Function that must be in the program for pyxel to work"""
    pyxel.cls(0)
    # pyxel.text(0, 0, "Trying stuff out", 3)
    # pyxel.text(0, 10, "party", pyxel.frame_count % 16)
    # x = pyxel.frame_count % pyxel.width
    # pyxel.text(x, 20, "tomaaa", 3)
    # layout_one = Layout()
    # layout_one.draw_floor()
    # layout_one.draw_platform()
    layout_two = Tilemap(0)
    layout_two.draw()
    # pyxel.blt(0, 210, 0, 0, 152, 16, 16)


pyxel.init(WIDTH, HEIGHT, title=CAPTION, fps=20, display_scale=3)
pyxel.load("assets/sprites-ssg-lpr.pyxres")
pyxel.run(update, draw)
