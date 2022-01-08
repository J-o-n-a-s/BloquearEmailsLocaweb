# Módulo de verificação do posicionamento

import pyautogui
import time


def posicionamento(x, y):
    pyautogui.moveTo(x=x, y=y)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 355, y=y + 255)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 825, y=y + 255)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 315, y=y + 80)
