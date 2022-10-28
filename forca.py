# Jogo da Forca

# Requisitos: Palavra oculta, numero de erros, sistema de acertos

def ocultar_palavra(palavra):
    palavra_ocultada_processada = []

    for letra in palavra:
        
        palavra_ocultada_processada.append('_')
        
    return palavra_ocultada_processada


palavra_oculta = 'desenho'
letras_ocultas = ocultar_palavra(palavra_oculta)
erros = 0

print(letras_ocultas)
