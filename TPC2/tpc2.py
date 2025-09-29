# %%
#TPC2 
#jogo dos fósforos

import random
primeira = True

print("Preparado para o jogo dos fósforos?") 
escolha=int(input("Escolhe se queres ser o primeiro ou o segundo jogador: "))
soma=21
print("Número inicial de fósforos: ", soma)
if escolha == 1:
    while soma > 1:
        questão = int(input("Escolhe um destes números (1, 2, 3 ou 4) para retirar ao número 21!"))
        if questão == 1 or questão == 2 or questão == 3 or questão == 4:
            if questão > soma:
                print("Não podes retirar mais fósforos que os disponíveis!")
                continue 
            print("O número escolhido foi: ", questão)
            soma = int(soma) - int(questão)
            print("Ficas-te com estes fósforos: " , int(soma))
            if soma ==1:
                print("Ganhaste!!")
                break
            computador = 5-questão
            if computador > soma - 1:
                computador=soma-1
            print("O computador escolheu: " , computador)
            soma = int(soma) - int(computador)
            print("Número de fósforos restantes: " , int(soma) - int(computador))
            if soma ==1:
                print("Perdeste!! Tenta de novo :)")
                break
        else:
            print("Escolhes-te o número errado!")

else:
    while soma > 1:
        if primeira == True:
            computador = random.randint(1,4)
            print("Computador escolheu o número: " , computador)
            soma = int(soma) - int(computador)
            print("Ficas-te com estes fósforos: ", int(soma)- int(computador))
            primeira = False
        questão = int(input("Escolhe um destes números (1, 2, 3 ou 4) para retirar ao número 21!"))
        if questão<=4 and questão>=1:
            if questão>soma:
                print("Não podes retirar mais fósforos que os disponíveis!")
                continue
            print("O número escolhido foi: ", questão)
            soma = int(soma) - int(questão)
            if soma == 1: 
                print("O computador ficou com estes fósforos: ")
                print("Ganhas-te!!!!")
                break
            else:
                print("Ficaste com estes fósforos: ", soma)
            computador = 5-questão
            if computador> soma-1:
                computador = soma-1
            print("Computador escolheu o número:", computador)
            soma = soma- computador
            print("Ficaste com estes fósforos: ", soma)
            if soma == 1:
                print("Perdeste :(")
                break
        else:
            print("Escolheste o número errado!!!")
            print("Começa de novo :)")


