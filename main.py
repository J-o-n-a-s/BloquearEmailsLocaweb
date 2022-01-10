# Programa principal

import PegarPosicaoNavegador as PePoNa
import BotAdicionarEmailsBloqueados as BoAdEmBl
import Posicionamento as Po

x = 0
y = 0

correto = ''
while correto != 'n':
    x, y = PePoNa.posicao_x_e_y()

    print('\nAgora você irá verificar os posicionamentos do cursor:')
    print('   1 - Canto superior esquerdo, onde você indicou o início do browser;')
    print('   2 - Campo onde deverão ser inseridos os e-mails que deverão ser bloqueados;')
    print('   3 - Botão "Adicionar" e-mails que serão bloqueados;')
    print('   4 - Botão "Salvar" lista de "Emails Bloqueados".')

    input('\nPressione enter para continuar.')

    seguinte = ''
    while seguinte != 'n':
        Po.posicionamento(x, y)
        seguinte = input('\nDeseja visualizar o posicionamento do cursor novamente? "s" para sim e "n" para não: ')

    correto = input('\nO posicionamento está incorreto? Deseja repetir o posicionamento?'
                    '\n"s" para sim e "n" para não: ')

BoAdEmBl.adicionar_emails(x, y)
input('\n\nPressione enter para continuar.')
