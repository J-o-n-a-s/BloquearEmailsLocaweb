# Módulo de verificação do posicionamento

import pyautogui
import time


def posicionamento(x, y):
    print('\nAgora você irá visualizar os posicionamentos do cursor:'
          '\n   1ª - Canto superior esquerdo, onde você indicou o início do browser;'
          '\n   2ª - Campo onde serão inseridos os e-mails/domínios que serão bloqueados/liberados;'
          '\n   3ª - Botão "Adicionar" e-mails que serão bloqueados/liberados;'
          '\n   4ª - Botão "Salvar" lista de "Emails Bloqueados"/"Emails Liberados".')

    input('\nPressione enter para continuar...')

    pyautogui.moveTo(x=x, y=y)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 355, y=y + 255)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 825, y=y + 255)
    time.sleep(1.5)
    pyautogui.moveTo(x=x + 315, y=y + 80)

    ret = input('\nDeseja visualizar o posicionamento do cursor novamente? "S" para sim e "N" para não: ')
    return ret
