# Módulo: Pegar a posição do navegador

import pyautogui
import time


def posicao_x_e_y():
    print('\nPosicione o cursor no lado superior esquerdo do seu navegador.')
    print('Você deve finalizar o posicionamento do cursor em até 5 segundos.')

    input('\nPressione enter para continuar...')

    for tempo in range(5):
        print(5 - tempo, end='')
        time.sleep(1)
        if tempo < 4:
            print(' - ', end='')

    x, y = pyautogui.position()
    print('\n\nA posição do cursor é: x = ' + str(x) + ' e y = ' + str(y))
    return x, y
