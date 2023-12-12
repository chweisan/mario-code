import pyxel

from constants import HEIGHT
from constants import WIDTH
from constants import PLAYING_AREA_START_X
from constants import PLAYING_AREA_START_Y
from constants import TILEMAP_START_X
from constants import TILEMAP_START_Y
from scoreboard import Map


class Tilemap:
    """in tiles, where each is 8x8"""

    def __init__(self, index: int):
        self.map = Map(WIDTH, HEIGHT)
        self.__index = index
        self.__floor_list = [(0, 16), (1, 16), (0, 17), (1, 17),
                             (2, 16), (2, 17), (3, 16), (3, 17)]
        self.__ceiling_list = [(2, 16), (2, 17), (3, 16), (3, 17)]
        # First tile is the floor to bump, the values are the bouncing floor for the block
        self.__ceiling_when_hit = {
            (2,17):[(4, 16), (5, 16), (6, 16)],
            (2,16):[(7, 16), (8, 16), (9, 16)],
            (3,17):[(10,16),(11,16),(12,16)],
            (3,16):[(13,16),(14,16),(15,16)]
            }

    @property
    def index(self) -> int:
        return self.__index

    @property
    def floor_list(self) -> list:
        return self.__floor_list

    @property
    def ceiling_list(self) -> list:
        return self.__ceiling_list

    def is_floor(self, floor: tuple) -> bool:
        return floor in self.__floor_list

    def is_ceiling(self, ceiling: tuple) -> bool:
        return ceiling in self.__ceiling_list

    def draw(self):
        pyxel.bltm(
            PLAYING_AREA_START_X,
            PLAYING_AREA_START_Y,
            self.index,
            u=TILEMAP_START_X,
            v=TILEMAP_START_Y,
            w=WIDTH,
            h=HEIGHT,
        )

    def get_tile(self, x, y):
        return pyxel.tilemap(self.index).pget(x // 8, y // 8)

    def get_tile_ceiling_index(self, x, y):
        ceiling_index = 0
        ceiling_index_left = 0
        ceiling_index_right = 0
        # If the tile at the left side of Mario is not in the list, catch the exception return 0
        try:
            tile_type_left  = pyxel.tilemap(self.index).pget(x // 8, y // 8)
            ceiling_index_left = list(self.__ceiling_when_hit.keys()).index(tile_type_left) + 1
        except ValueError:
            pass
        ceiling_index = ceiling_index_left            

        # If the tile at the right side of Mario is not in the list, catch the exception return 0
        try:
            tile_type_right = pyxel.tilemap(self.index).pget((x+8) // 8, y // 8)
            ceiling_index_right = list(self.__ceiling_when_hit.keys()).index(tile_type_right) + 1
        except ValueError:
            pass

        # Return always the one at the left, but if not in the list, return the one at the right
        # if possible
        if ceiling_index_right > ceiling_index:
            ceiling_index = ceiling_index_right
        return ceiling_index
        

