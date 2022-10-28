# Jogo da Forca

# Requisitos: Palavra oculta, numero de erros, sistema de acertos

# Funções utiizadas: 
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

# Mensagens utilizadas

perdedor = 'Você infelizmente gastou todas as suas tentativas e perdeu :/'
mensagem_chute = 'Qual letra você acha que existe na palavra oculta?\n'

# Propriedades e requisitos para funcionamento do jogo

palavra_oculta = 'desenho'
letras_ocultas = ocultar_palavra(palavra_oculta)
erros = 0
max_erros = 6
acertou = False
enforcou = False

# Estrutura do jogo

while not acertou and not enforcou:
    print(letras_ocultas)
    print(mensagem_max_erros(max_erros, erros))
    letra_chutada = input(mensagem_chute).lower()

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

    acertou = '_' not in letras_ocultas
    enforcou = erros == max_erros

if acertou:
    print(ganhador(erros))
elif enforcou:
    print(perdedor)