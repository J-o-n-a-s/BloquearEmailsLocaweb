# Módulo: Adicionar lista de e-mails que devem ser bloqueados pelo servidor da Locaweb

import pyautogui
import time
import sys

pyautogui.PAUSE = 0.15


def leitura_arquivo():
    while True:
        caminho = input('\nPor gentileza digite o caminho completo do arquivo txt que deseja importar: ')
        ret, linhas = _abrir_arquivo(caminho)
        if ret == 0:
            break

        else:
            correto = input('Deseja retentar? "S" para sim e "N" para não: ')
            if correto.lower() == 'n':
                break

    return ret, linhas


def _abrir_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError as erro:
        _log_error(str(sys.exc_info()[0]), erro)
        print(f'\nNão foi possível abrir o arquivo. Verifique o caminho e o nome do arquivo.')
        return 1, ''
    except OSError as erro:
        _log_error(str(sys.exc_info()[0]), erro)
        print(f'\nNão foi possível abrir o arquivo. Verifique o caminho e o nome do arquivo.')
        return 1, ''
    else:
        return 0, linhas


def _log_error(exception, erro):
    with open('\\log\\' + str(time.strftime("%x")) + '.log', 'w') as arquivo:
        arquivo.write(f'{str(time.strftime("%X"))} - {exception} - {erro}')


def adicionar_emails(x, y, linhas):
    inicio = time.time()
    print(f'\nProcesso iniciado às {time.strftime("%x %X")}.')
    try:
        for linha in linhas:
            pyautogui.leftClick(x=x + 355, y=y + 255)
            pyautogui.write(linha)
            pyautogui.leftClick(x=x + 825, y=y + 255)
    except KeyboardInterrupt as erro:
        _log_error(str(sys.exc_info()[0]), erro)
        print('\nImportação da lista de e-mails não concluída corretamente!')
    else:
        pyautogui.leftClick(x=x + 315, y=y + 80)
        fim = time.time()
        print(f'Processo finalizado às {time.strftime("%x %X")}.'
              f'\nTempo total de {(fim - inicio):.2f} segundos.')
        print('\nFim da importação da lista de e-mails que serão bloqueados/liberados!')
