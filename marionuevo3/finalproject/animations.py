import pyxel
from constants import WIDTH
from constants import HEIGHT
from constants import FPS


class Animation:
    """Class to store and display a single animation"""

    def __init__(self, steps: list, fps: int, x_size: int, y_size: int):
        # Given the list of animation steps and the fps, we can calculate the
        # different animation frames for each step of the animation

        # Each step is composed of:
        # - The number of seconds (as a float) that the step lasts
        # - A list of the tiles that compose the step according to the
        #   passed x_size and y_size:
        #   - The duple of the tile in the tilemap that corresponds to the step
        #   - The index of the tilemap that corresponds to the tile
        #
        # Example:
        # We have a 2x2 tile (16x16) and we want to animate it with four steps
        # of 1.0 seconds each. And the tilemap index is 0.
        # We would have:
        # steps = [
        #     [1.0, [((25,0), 0), ((26,0), 0], ((27,0),0), ((28,0),0))],
        #     [1.0, [((35,0), 0), ((36,0), 0], ((37,0),0), ((38,0),0))],
        #     [1.0, [((35,0), 0), ((36,0), 0], ((37,0),0), ((38,0),0))],
        #     [1,0, [((25,0), 0), ((26,0), 0], ((27,0),0), ((28,0),0))]]

        # We store the x_size and y_size to
        self.__x_size = x_size
        self.__y_size = y_size

        # We store the steps for each frame of the animation
        self.__steps = []
        for step in steps:
            # We calculate the number of frames for each step
            frames_per_step = int(step[0] * fps)
            # Now we need to store the frames for each step
            for i in range(frames_per_step):
                # We calculate the frame for each step
                self.__steps.append(step[1])

    def __len__(self):
        """Returns the number of frames in the animation"""
        return len(self.__steps)

    def draw(self, x: int, y: int, frame: int):
        """Draws the animation frame in the given position
        x: absolute position of the animation in the game canvas
        y: absolute position of the animation in the game canvas
        frame: the frame to draw in the animation object
        """
        # We have to draw the animation in the position of x and y
        # parameters passed to the method, but also considering the
        # size of the animation (x_size and y_size)
        TILE_X_SIZE = 8
        TILE_Y_SIZE = 8
        for j in range(self.__y_size):
            for i in range(self.__x_size):
                # We calculate the tilemap index for the given frame
                (tile, tilemap_index) = self.__steps[frame][
                    i + (j * self.__x_size)]
                # We draw the tilemap in the given position
                pyxel.blt(
                    x + i * TILE_X_SIZE,
                    y + j * TILE_Y_SIZE,
                    tilemap_index,
                    tile[0],
                    tile[1],
                    TILE_X_SIZE,
                    TILE_Y_SIZE,
                )


class Animations:
    """Class to manage a set of animations"""

    def __init__(self):
        # Here we define all the animations needed by the game and we
        # assign an identifier to each one to easily reference
        # them in the game

        # Ceiling bump animation
        ceiling_bump_1 = Animation(
            [
                [
                    0.2,
                    [
                        ((32, 128), 0),
                        ((40, 128), 0),
                        ((48, 128), 0),
                        ((32, 136), 0),
                        ((40, 136), 0),
                        ((48, 136), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((16, 136), 0),
                        ((16, 136), 0),
                        ((16, 136), 0),
                    ],
                ],
            ],
            FPS,
            3,
            2,
        )
        ceiling_bump_2 = Animation(
            [
                [
                    0.2,
                    [
                        ((56, 128), 0),
                        ((64, 128), 0),
                        ((56, 136), 0),
                        ((64, 136), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((16, 128), 0),
                        ((16, 128), 0),
                    ],
                ],
            ],
            FPS,
            2,
            2,
        )
        ceiling_bump_3 = Animation(
            [
                [
                    0.2,
                    [
                        ((72, 128), 0),
                        ((80, 128), 0),
                        ((88, 128), 0),
                        ((72, 136), 0),
                        ((80, 136), 0),
                        ((88, 136), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((24, 136), 0),
                        ((24, 136), 0),
                        ((24, 136), 0),
                    ],
                ],
            ],
            FPS,
            3,
            2,
        )

        ceiling_bump_4 = Animation(
            [
                [
                    0.2,
                    [
                        ((96, 128), 0),
                        ((104, 128), 0),
                        ((112, 128), 0),
                        ((96, 136), 0),
                        ((104, 136), 0),
                        ((112, 136), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((64, 248), 0),
                        ((24, 128), 0),
                        ((24, 128), 0),
                        ((24, 128), 0),
                    ],
                ],
            ],
            FPS,
            3,
            2,
        )


        # POW animation
        pow = Animation(
            [
                [
                    0.3,
                    [
                        ((0, 168), 0),
                        ((8, 168), 0),
                        ((0, 176), 0),
                        ((8, 176), 0),
                    ],
                ],
                [
                    0.3,
                    [
                        ((16, 168), 0),
                        ((24, 168), 0),
                        ((16, 176), 0),
                        ((24, 176), 0),
                    ],
                ],
                [
                    0.3,
                    [
                        ((32, 168), 0),
                        ((40, 168), 0),
                        ((32, 176), 0),
                        ((40, 176), 0),
                    ],
                ],
                [
                    0.3,
                    [
                        ((32, 168), 0),
                        ((40, 168), 0),
                        ((32, 176), 0),
                        ((40, 176), 0),
                    ],
                ],
                [
                    0.3,
                    [
                        ((16, 168), 0),
                        ((24, 168), 0),
                        ((16, 176), 0),
                        ((24, 176), 0),
                    ],
                ],
                [
                    0.3,
                    [
                        ((0, 168), 0),
                        ((8, 168), 0),
                        ((0, 176), 0),
                        ((8, 176), 0),
                    ],
                ],
            ],
            FPS,
            2,
            2,
        )
        # coin bonus animation
        bonus_coin = Animation(
            [
                [
                    0.3,
                    [
                        ((120, 96), 0)
                    ],
                ],
                [
                    0.3,
                    [
                        ((56, 104), 0)
                    ],
                ],
                [
                    2,
                    [
                        ((48, 104), 0),
                    ],
                ],
                [
                    0.1,
                    [
                        ((56, 104), 0)
                    ],
                ],
                [
                    0.1,
                    [
                        ((120, 96), 0)
                    ],
                ],
            ],
            FPS,
            1,
            1,
        )

        mario_dying = Animation(
            [
                [
                    0.2,
                    [
                        ((96, 0), 0),
                        ((104, 0), 0),
                        ((96, 8), 0),
                        ((104, 8), 0),
                        ((96, 16), 0),
                        ((104, 16), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((96, 0), 0),
                        ((104, 0), 0),
                        ((96, 8), 0),
                        ((104, 8), 0),
                        ((96, 16), 0),
                        ((104, 16), 0),
                    ],
                ],
                [
                    0.2,
                    [
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                        ((96, 48), 0),
                    ],
                ],
            ],
            FPS,
            2,
            3,
        )

        shellcreeper_upside = Animation(
            [
                [
                    0.2,
                    [
                        ((32, 32), 0),
                        ((40, 32), 0),
                        ((32, 40), 0),
                        ((40, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((48, 32), 0),
                        ((54, 32), 0),
                        ((48, 40), 0),
                        ((54, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((32, 32), 0),
                        ((40, 32), 0),
                        ((32, 40), 0),
                        ((40, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((48, 32), 0),
                        ((54, 32), 0),
                        ((48, 40), 0),
                        ((54, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((32, 32), 0),
                        ((40, 32), 0),
                        ((32, 40), 0),
                        ((40, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((48, 32), 0),
                        ((54, 32), 0),
                        ((48, 40), 0),
                        ((54, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((32, 32), 0),
                        ((40, 32), 0),
                        ((32, 40), 0),
                        ((40, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((48, 32), 0),
                        ((54, 32), 0),
                        ((48, 40), 0),
                        ((54, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((32, 32), 0),
                        ((40, 32), 0),
                        ((32, 40), 0),
                        ((40, 40), 0)
                    ],
                ],
                [
                    0.2,
                    [
                        ((48, 32), 0),
                        ((54, 32), 0),
                        ((48, 40), 0),
                        ((54, 40), 0)
                    ],
                ],
            ],
            FPS,
            2,
            2,
        )

        bigentity_dying = Animation(
            [
                [
                    0.4,
                    [
                        ((80, 80), 0),
                        ((88, 80), 0),
                        ((80, 88), 0),
                        ((88, 88), 0)
                    ],
                ],
                [
                    0.4,
                    [
                        ((48, 112), 0),
                        ((56, 112), 0),
                        ((48, 120), 0),
                        ((56, 120), 0)
                    ],
                ],
                [
                    0.4,
                    [
                        ((64, 112), 0),
                        ((72, 112), 0),
                        ((64, 120), 0),
                        ((72, 120), 0)
                    ],
                ],
                [
                    0.4,
                    [
                        ((80, 112), 0),
                        ((88, 112), 0),
                        ((80, 120), 0),
                        ((88, 120), 0)
                    ],
                ],
                [
                    0.4,
                    [
                        ((96, 112), 0),
                        ((104,112), 0),
                        ((96, 120), 0),
                        ((104,120), 0)
                    ],
                ],
            ],
            FPS,
            2,
            2,
        )







        self.__animations = {}
        self.__animations["CEILING_BUMP_1"] = ceiling_bump_1
        self.__animations["CEILING_BUMP_2"] = ceiling_bump_2
        self.__animations["CEILING_BUMP_3"] = ceiling_bump_3
        self.__animations["CEILING_BUMP_4"] = ceiling_bump_4
        self.__animations["POW"] = pow
        self.__animations["BONUS_COIN"] = bonus_coin
        self.__animations["MARIO_DYING"] = mario_dying
        self.__animations["SHELLCREEPER_UPSIDE"] = shellcreeper_upside
        self.__animations["BIGENTITY_DYING"] = bigentity_dying

        # We store the active animations here, and we should
        # check them on every frame to see if they are finished
        self.__active_animations = {}

        # We initialize the animation id counter
        self.__animation_id = 0

    @property
    def animation_id(self):
        """Returns the animation id counter"""
        return self.__animation_id

    @property
    def active_animations(self):
        """Returns the active animations"""
        return self.__active_animations

    def add(self, animation_name: str, x: int, y: int, loop: bool) -> int:
        """Starts an animation with the given name in the given position"""
        # We check if the animation exists
        if animation_name not in self.__animations:
            return -1

        # We increment the animaion Id counter and we return it to the caller
        current_animation_id = self.__animation_id
        self.__active_animations[current_animation_id] = {
            "animation": self.__animations[animation_name],
            "animation_name": animation_name,
            "frame": 0,
            "x": x,
            "y": y,
            "loop": loop,
        }
        self.__animation_id += 1
        return current_animation_id

    def draw(self):
        """Draws all the active animations"""
        force_delete_animation = []
        force_reloop = []
        for animation_id, current_animation in self.active_animations.items():
            # anomation_id is the key of the dictionary
            current_frame = current_animation["frame"]
            current_x = current_animation["x"]
            current_y = current_animation["y"]
            current_loop = current_animation["loop"]
            current_animation["animation"].draw(current_x, current_y,
                                                current_frame)
            current_frame += 1
            if current_frame >= len(current_animation["animation"]):
                # The animation is finished, we remove it from the active
                # animations
                # We cannot remove the item from the dictionary while iterating
                if current_loop:
                    force_reloop.append(animation_id)
                else:
                    force_delete_animation.append(animation_id)
            else:
                # We update the frame in the active animations
                current_animation["frame"] = current_frame

        # We remove the finished animations
        for animation_id in force_delete_animation:
            del self.active_animations[animation_id]

        # We reloop the animations
        for animation_id in force_reloop:
            self.active_animations[animation_id]["frame"] = 0

    def exist_active(self, animation_name) -> bool:
        found = False
        for item in self.__active_animations.values():
            if item["animation_name"] == animation_name:
                found = True
        return found
