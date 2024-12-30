import ctypes
from typing import List

def get_screen_resolution() -> List[int]:
    # return width, height of screen
    user32 = ctypes.windll.user32
    screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    # print(screensize)
    return screensize
