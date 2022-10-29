import forca
import adivinhacao
import os

def limpar_tela():
    os.system('cls')

menu_mensagem_intro = 'Olá, bem vindx ao centro de jogos!\nPara sair, digite \'sair\'.\nO que deseja jogar hoje?'
jogos_disponiveis = 'F) Forca\nA) Adivinhação\n'
agradecimento_saida = 'Obrigado por jogar conosco!\nPressione enter para sair.\n'
erro_escolha = 'A opção selecionada não é válida!\nEscolha entre:\n'

escolha = False

print(menu_mensagem_intro)
escolha = input(jogos_disponiveis).lower()

while escolha != 'sair' and escolha != 'f' and escolha != 'a':
    limpar_tela()
    print(erro_escolha)
    escolha = input(jogos_disponiveis).lower()

limpar_tela()

if escolha == 'f':
    forca.jogar()
elif escolha == 'a':
    adivinhacao.jogar()
elif escolha == 'sair':
    input(agradecimento_saida)

