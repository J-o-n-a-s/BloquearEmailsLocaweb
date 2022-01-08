# Módulo: Adicionar lista de e-mails que devem ser bloqueados pelo servidor da Locaweb

import pyautogui

pyautogui.PAUSE = 0.15


def adicionar_emails(x, y):
    caminho = input('\nPor gentileza digite o caminho completo do arquivo txt que deseja importar: ')
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        pyautogui.leftClick(x=x + 355, y=y + 255)
        pyautogui.write(linha)
        pyautogui.leftClick(x=x + 825, y=y + 255)

    pyautogui.leftClick(x=x + 315, y=y + 80)

    print('\nFim da importação da lista de e-mails que serão bloqueados!')
