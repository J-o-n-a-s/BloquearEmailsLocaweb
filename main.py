'''
Antes de tudo:

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor do que complicado.
Plano é melhor do que aninhado.
Esparso é melhor do que denso.
A legibilidade conta.
Casos especiais não são especiais o suficiente para quebrar as regras.
Embora a praticidade supere a pureza.
Os erros nunca devem passar silenciosamente.
A menos que explicitamente silenciado.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver uma - e de preferência apenas uma - maneira óbvia de fazer isso.
Embora essa maneira possa não ser óbvia no início, a menos que você seja holandês.
Agora é melhor do que nunca.
Embora nunca seja melhor do que *agora*.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação for fácil de explicar, pode ser uma boa ideia.
Namespaces são uma ótima ideia -- vamos fazer mais desses!
'''

# Programa principal

import PegarPosicaoNavegador as PePoNa
import BotAdicionarEmailsBloqueados as BoAdEmBl
import Posicionamento as Po
import ctypes

print('O objetivo deste programa é inserir uma lista de e-mails/domínios no servidor de e-mails da Locaweb'
      ' a partir de um arquivo texto.\nCada linha do arquivo deverá conter um único e-mail ou domínio.')
bloquear = input('\nDeseja bloquear a máquina no final da execução do programa?\n"S" para sim e "N" para não: ')

while True:
    x, y = PePoNa.posicao_x_e_y()

    while True:
        seguinte = Po.posicionamento(x, y)
        if seguinte.lower() == 'n':
            break

    correto = input('\nO posicionamento está incorreto? Deseja repetir o posicionamento?'
                    '\n"S" para sim e "N" para não: ')
    if correto.lower() == 'n':
        break

ret, arquivo = BoAdEmBl.leitura_arquivo()

if ret == 0:
    BoAdEmBl.adicionar_emails(x, y, arquivo)
else:
    print('\n Infelizmente não foi possível concluir a execução do programa corretamente.', end='')

if bloquear.lower() == 's':
    ctypes.windll.user32.LockWorkStation()

input('\n\nPressione enter para finalizar o programa...')
