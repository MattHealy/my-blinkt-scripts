from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)

SLEEP = 0.05

PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLOURS = [PURPLE, RED, GREEN, BLUE]


while True:

    for col in COLOURS:
        for i in range(4):
            clear()
            set_pixel(i, col[0], col[1], col[2])
            set_pixel(7-i, col[0], col[1], col[2])
            show()
            time.sleep(SLEEP)
        for i in reversed(range(4)):
            clear()
            set_pixel(i, col[0], col[1], col[2])
            set_pixel(7-i, col[0], col[1], col[2])
            show()
            time.sleep(SLEEP)
