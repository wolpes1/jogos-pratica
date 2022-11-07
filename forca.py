# Jogo da Forca

import os
import random

# Requisitos: Palavra oculta, numero de erros, sistema de acertos

# Funções utiizadas: 

# Limpar os dados da tela

def limpar_tela():
    os.system('cls')

# Criar uma array com a quantidade de traços para mostrar as letras da palavra

def ocultar_palavra(palavra):
    palavra_ocultada_processada = []

    for letra in palavra:
        palavra_ocultada_processada.append('_')
        
    return palavra_ocultada_processada

# Função para mostrar a quantidade de erros cometidos e a que podem ser cometidos ainda

def mensagem_max_erros(max_erros, erros):
    return(f'Você errou {erros} vezes de um máximo de {max_erros}.')

# Função para mostrar ao ganhador com quantos erros ele ganhou

def ganhador(erros):
    return(f'Parabéns! Você ganhou com apenas {erros} erros!')

# Função para obter palavra de um arquivo

def obter_palavra(arquivo = str):

    palavras = []
    with open(arquivo, 'r') as arquivo_aberto:
        for linha in arquivo_aberto:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))

    palavra_aleatoria = palavras[numero]

    return palavra_aleatoria


# Estrutura do jogo

def jogar():

    # Mensagens utilizadas

    perdedor = 'Você infelizmente gastou todas as suas tentativas e perdeu :/'
    mensagem_chute = 'Qual letra você acha que existe na palavra oculta?\n'
    letra_usada = 'Esta letra já foi usada!'

    # Propriedades e requisitos para funcionamento do jogo

    letras_chutadas = []
    palavra_oculta = obter_palavra('palavras.txt')
    letras_ocultas = ocultar_palavra(palavra_oculta)
    erros = 0
    max_erros = 6
    acertou = False
    enforcou = False
    boas_vindas = 'Olá, bem vindx ao Jogo da forca! Vamos começar?\nPressione enter para continuar.\n'

    input(boas_vindas)

    while not acertou and not enforcou:
        limpar_tela()
        print(letras_ocultas)
        print(mensagem_max_erros(max_erros, erros))
        letra_chutada = input(mensagem_chute).lower()
        

        if letra_chutada in letras_chutadas:
            input(letra_usada)
        else:
            if letra_chutada in palavra_oculta:
                position = 0
                for letra in palavra_oculta:
                    if letra == letra_chutada:
                        letras_ocultas[position] = letra_chutada
                        position += 1
                    else:
                        position += 1
            else:
                erros += 1

        letras_chutadas.append(letra_chutada)
        acertou = '_' not in letras_ocultas
        enforcou = erros == max_erros

    if acertou:
        print(f'A palavra oculta era {palavra_oculta}!')
        print(ganhador(erros))
        input('Pressione enter para sair.')
    elif enforcou:
        print(perdedor)
        input('Pressione enter para sair')