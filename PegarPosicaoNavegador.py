# Módulo: Pegar a posição do navegador

import pyautogui
import time


def posicao_x_e_y():
    print('\nPosicione o cursor na parte superior esquerdo do seu navegador.')
    print('Você deve finalizar o posicionamento do cursor em 5 segundos.')

    input('\nPressione enter para continuar.')

    tempo = 6
    while tempo > 1:
        tempo -= 1
        print(tempo)
        time.sleep(1)

    x, y = pyautogui.position()
    print('\nA posição do cursor é: x = ' + str(x) + ' e y = ' + str(y))
    return x, y
