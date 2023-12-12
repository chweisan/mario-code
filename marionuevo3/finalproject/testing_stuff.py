import pyxel
from constants import constant

position = [10, 10]


def move(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        x = x + 1
    elif pyxel.btn(pyxel.KEY_LEFT):
        x = x - 1
    elif pyxel.btn(pyxel.KEY_UP):
        y = y - 1
    elif pyxel.btn(pyxel.KEY_DOWN):
        y = y + 1

    return x, y


def update():
    if pyxel.btnp(pyxel.KEY_ESCAPE):
        pyxel.quit()
    else:
        position[0], position[1] = move(position[0], position[1])


def draw():
    pyxel.cls(0)
    pyxel.text(0, 0, "Trying stuff out", 3)
    pyxel.text(0, 10, "party", pyxel.frame_count % 16)
    x = pyxel.frame_count % pyxel.width
    pyxel.text(x, 20, "tomaaa", 3)
    pyxel.blt(position[0], position[1], 0, 0, 0, 16, 24)


pyxel.init(WIDTH, HEIGHT, title=CAPTION)
pyxel.load("assets/sprites-ssg-lpr.pyxres")
pyxel.run(update, draw)
