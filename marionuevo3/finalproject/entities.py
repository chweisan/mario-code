import random
import pyxel
from constants import GRAVITY
from constants import SPRITE_SPEED_X
from constants import HEIGHT
from constants import FPS

class Entities:
    def __init__(self, x: int, y: int, w: int, h: int):
        """:param x: int,
        :param y: int
        :param w: int
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_vel = 0
        self.y_vel = 0
        self.sprite = [0, 0, 0, 0, 0]
        self.angry_attribute = False
        self.lives = 0
        self.upside_down_delay = 5 # seconds
        self.upside_down_delay_frames = self.__upside_down_delay * FPS
        # all these values that are 0 will be defined when the child classes are initialized

        self.gravity = GRAVITY
        self.direc = None  # will be defined when we generate the element
        self.gen = False  # this tells us if the sprite has been fully generated and created on the screen
        self.ungen = False  # for when it un-generates upon reaching a tube
        self.upsd = False  # upside down state
        self.normal = True  # if they are normal state or the color changes
        #        self.angry = False  # only for sidesteppers, but if not defined here, animation function will have problems
        self.width = 0  # will be defined for each entity in their own separate class
        self.height = 0

        self.anim = {}
        self.__counter = 0
        # In the dictionary above (according to the numbering below), we give a starting sprite value, and the last
        # sprite value inside an animation
        # 1: normal
        # 2: normal, upside-down
        # 3: after color change
        # 4: after color change, upside-down
        # 5: normal, angry (crabs)
        # 6: after color change, angry (crabs)

        self.in_side()

    @property
    def upside_down_delay(self):
        return self.__upside_down_delay
    
    @upside_down_delay.setter
    def upside_down_delay(self, value):
        self.__upside_down_delay = value
        self.upside_down_delay_frames = self.__upside_down_delay * FPS

    @property
    def upside_down_delay_frames(self):
        return self.__upside_down_delay_frames
    
    @upside_down_delay_frames.setter
    def upside_down_delay_frames(self, value):
        self.__upside_down_delay_frames = value

    @property
    def is_upside_down(self):
        return self.upsd

    def move(self, x_vel, y_vel):
        self.x += x_vel
        self.y -= y_vel
        if self.x >= (self.w + 1):  # again, how to make the sprites move to the other edge once out of range
            self.x = 0
        elif self.x <= (-1):
            self.x = self.w

    # change dir would be used when there's a collision, and they change direction: changes the velocity and image
    def change_dir(self):
        if self.direc:  # when direction is true, it's going right
            self.direc = False  # so now they go left
            self.x_vel = -self.x_vel    # the speed is inverted
            self.sprite[3] = -self.sprite[3]    # and so is the image
        elif not self.direc:    # same when they're going left, everything is inverted
            self.direc = True
            self.x_vel = -self.x_vel
            self.sprite[3] = -self.sprite[3]

    def loop(self):
        self.y_vel -= self.gravity
        self.move(self.x_vel, self.y_vel)

    def in_side(self):  # a form to randomly generate the side where they will appear
        side = random.randint(0, 1)
        if side == 0:  # appears on the left, moves to right
            self.direc, self.x, self.x_vel = True, 48, self.x_vel
        else:
            self.direc, self.x, self.x_vel = False, self.w - 32 - 16, -self.x_vel

    def loop_gen(self):
        if self.direc:      # to slowly generate the image:
            if self.sprite[3] < self.width:
                # we will slowly add pixels to the width of the image until it reaches the correct width,
                # particular to each entity
                self.sprite[3] += 1     # so we add one pyxel each time to the width
                self.sprite[1] -= 1     # but since we want to see the sprite generate slowly,
                # starting with the front of it, we slowly decrease the u position of the image.
                # That is, the u position was initially set on the edge of the image, where the front would be.
                # But as the width starts increasing, we must show more of the image,
                # and we move the u starting point to the left.
            else:   # and once the image has been generated, this stops, and we give the moving values
                self.gen = True
                self.gravity, self.x_vel = GRAVITY, SPRITE_SPEED_X
        else:   # this process would be inverted when the sprite is on the right
            if -self.sprite[3] < self.width:
                self.sprite[3] -= 1     # instead of adding, we take one less, since the image is, after all, inverted
                self.sprite[1] -= 1
                self.x -= SPRITE_SPEED_X//2     # this is just to compensate, otherwise the image would go backwards
            else:
                self.gen = True
                self.gravity, self.x_vel = GRAVITY, -SPRITE_SPEED_X


    def reach_tube(self):
        return ((not self.direc and self.x == self.w - 40 and self.y == HEIGHT - 16 - self.sprite[4]) or
                (self.direc and self.x - self.width == 40 and self.y ==
                 HEIGHT - 16 - self.sprite[4]))

    def upside_down(self):
        # if the object was already upside down, they would stand up again:
        if self.upsd:
            self.upsd = False
            if self.direc:
                self.x_vel = SPRITE_SPEED_X
            else:
                self.x_vel = -SPRITE_SPEED_X
            if self.normal:
                self.sprite[1] = self.anim[1][0]
            if not self.normal:
                self.sprite[1] = self.anim[3][0]
                self.x_vel *= 2
        # if the object wasn't upside down, now it is
        else:
            self.upsd = True
            if self.normal:
                self.sprite[1] = self.anim[2][0]
            if not self.normal:
                self.sprite[1] = self.anim[4][0]
            self.x_vel = 0

    def angry(self):
        """This method is optional. Should be implemented only if the
        creature can be angry"""

    def animation(self):
        # so we have to put all the combinations for the animation
        # 1. Not upsidedown, normal state
        # 2. Upsidedown, normal state
        # 3. Not upsidedown, color changed state
        # 4. Upsidedown, color changed state
        self.__counter += 2
        if self.__counter == self.width:
            self.sprite[1] += self.width  # so the u image value moves from sprite to sprite
            self.__counter = 0
        if not self.upsd and self.normal:
            # once the limit is reached, it starts all over again
            if self.sprite[1] >= self.anim[1][1]:
                self.sprite[1] = self.anim[1][0]
        elif self.upsd and self.normal:
            if self.sprite[1] >= self.anim[2][1]:
                self.sprite[1] = self.anim[2][0]
        elif not self.upsd and not self.normal:
            if self.sprite[1] >= self.anim[3][1]:
                self.sprite[1] = self.anim[3][0]
        elif self.upsd and not self.normal:
            if self.sprite[1] >= self.anim[4][1]:
                self.sprite[1] = self.anim[4][0]

    def update(self):
        self.animation()
        if not self.gen:    # if it hasn't been generated, the speed will be 0
            self.gravity = self.y_vel = self.x_vel = 0
            self.loop_gen()
        elif self.gen and not self.ungen:   # else, we have that it all works normally
            if self.y_vel - self.gravity < -8:
                self.y_vel = -8 + self.gravity
            self.loop()
        """elif self.ungen:
            self.gravity = self.y_vel = self.x_vel = 0
            self.loop_degen()"""
        
    def draw(self):
        """Draws the entity on the screen"""
        pyxel.blt(self.x, self.y, *self.sprite, colkey=0)

class Coin(Entities):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.sprite = [0, 8, 104, 0, 8]
        self.width = 8
        self.height = 8
        # The format of the animation is: (seconds, u, v)
        # this is custom built because I couldn't make it work with the other animation
        self.anim = [(0.1,8, 104), (0.1,16, 104), (0.1,24, 104), (0.1,32, 104), (0.1, 40, 104)]
        self.__anim_frames = []
        for (secs, coord_x, coord_y) in self.anim:
            for _ in range(int(secs * FPS)):
                self.__anim_frames.append((coord_x, coord_y))
        self.__current_anim_frames_count = len(self.__anim_frames)
        self.__counter = 0

    # particular animation for coin cause it moves a bit faster than the others
    def draw(self):
        pyxel.blt(self.x, self.y, 0, *self.__anim_frames[self.__current_anim_frames_count], self.width, self.height, colkey=0)

    def animation(self):
        # custom animation function to simply animate the coins
        if (self.__current_anim_frames_count > 0):
            self.__current_anim_frames_count -= 1
        else:
            self.__current_anim_frames_count = len(self.__anim_frames) -1

class Shellcreeper(Entities):
    def __init__(self, x, y, w: int, h: int):
        super().__init__(x, y, w, h)
        self.x, self.y = x, y
        self.sprite = [0, 16, 32, 0, 16]
        self.width = 16
        self.height = 16
        self.lives = 1
        self.x_vel = 0
        self.y_vel = 0
        self.gravity = GRAVITY
        self.anim = {1: (0, 16), 2: (32, 48), 3: (80, 96), 4: (112, 128)}
        self.upside_down_delay = 2  # seconds
        self.in_side()

    def upside_down(self):
        # if the object was already upside down, they would stand up again:
        self.upsd = not self.upsd

    def draw(self):
        if self.upsd:
            if self.upside_down_delay_frames > 0:
                self.upside_down_delay_frames -= 1
            else:
                self.upside_down_delay_frames = self.upside_down_delay * FPS
                self.upsd = False
        else:
            pyxel.blt(self.x, self.y, *self.sprite, colkey=0)

    def loop(self):
        if not self.upsd:
            super().loop()


class Sidestepper(Entities):
    def __init__(self, x, y, w, h: int):
        super().__init__(x, y, w, h)
        self.x, self.y = x, y
        self.sprite = [0, 16, 64, 0, 16]
        self.width = 16
        self.height = 16
        self.lives = 2
        self.x_vel = 0
        self.angry_attribute = False    # to add an extra to the animation
        self.anim = {1: (0, 32), 2: (64, 48), 3: (96, 128), 4: (160, 192), 5: (32, 64), 6: (128, 160)}
        # 5. Angry, but normal
        # 6. Angry after color change
        self.in_side()

    def angry(self):
        self.angry_attribute = True
        if self.normal:
            self.sprite[1] = self.anim[5][0]
            self.x_vel *= 2
        if not self.normal:
            self.sprite[1] = self.anim[6][0]
            self.x_vel *= 4

class Fly(Entities):
    def __init__(self, x, y, w, h: int):
        super().__init__(x, y, w, h)
        self.x, self.y = x, y
        self.sprite = [0, 16, 48, 0, 16]
        self.width = 16
        self.height = 16
        self.lives = 1
        self.jumping = False
        self.anim = {1: (0, 48), 2: (48, 80)}
        self.in_side()