import random

def jogar():
    print("Bem vindo ao pedra , papel ou tesoura!")
    opcoes =["pedra" , "papel" , "tesoura"]
    while True:
#escolha do jogador
        jogador = input("escolha pedra, papel ou tesoura (ou 'sair' para encerrar) : ").lower()
        if jogador == "sair":
            print("Obrigado por jogar!")
            break
        if jogador not in opcoes:
            print("opcão invalida. tente novamente.")
            continue
#escolha do computador
        computador = random.choice (opcoes)
        print(f"computador escolheu : {computador}")
#determinar vencedor
        if jogador == computador:
            print("empate!")
        elif (jogador == "pedra" and computador == "tesoura")or \
            (jogador == "papel" and computador == "pedra")or \
            (jogador == "tesoura"and computador == "papel"):
            print("você venceu!")
        else:
            print("você perdeu:")
        print()
jogar()
