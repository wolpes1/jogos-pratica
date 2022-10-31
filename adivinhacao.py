# Jogo de adivinhação

# Requisitos: Numero Oculto, Número de Tentativas, Sistema de acertos

import random
import os

def obter_numero(numero_maximo):
    return random.randint(0, numero_maximo)

def limpar_tela():
    os.system('cls')


def jogar():
    facil = obter_numero(10)
    medio = obter_numero(20)
    dificil = obter_numero(30)

    tentativas = 10
    numero_oculto = None
    acertou = False

    dificuldade = None

    while dificuldade == None:
        print('Em qual dificuldade você deseja jogar?\n')
        dificuldade = input('F) Fácil\nM) Médio\nD) Difícil\n').lower()
        if dificuldade != 'f' and dificuldade != 'm' and dificuldade != 'd':
            print('Esta não é uma opção válida!')
            dificuldade = None

    if dificuldade == 'f':
        numero_oculto = facil
    elif dificuldade == 'm':
        numero_oculto = medio
    elif dificuldade == 'd':
        numero_oculto = dificil

    while tentativas != 0 and acertou != True:
        print(f'Você tem {tentativas} tentativas para acertar o número.')
        print('Qual número você deseja chutar?\n')
        numero_chutado = int(input('Insira o número: '))
        if numero_chutado > numero_oculto:
            print(f'O número {numero_chutado} é maior que o oculto.')
            tentativas -= 1
        elif numero_chutado < numero_oculto:
            print(f'O número {numero_chutado} é menor que o oculto.')
            tentativas -= 1
        else:
            acertou = True
            break

    if tentativas == 0:
        print('Você perdeu :(')
        input('Pressione enter para sair.')
    elif acertou:
        print(f'Você adivinhou o número oculto, que era {numero_oculto}!')
        input('Pressione enter para sair.')
