# %%
#tpc3

Lista =[]
import random




def CriaLista (N):
    global Lista
    n = 1
    Lista = []
    while  n <= N:
        Lista.append(random.randint(1,100))
        n = n + 1
    return Lista

def LeLista(N):
    global Lista
    res=[]
    for i in range (N):
        num = int(input(f"Introduza um número {i+1}/{N}"))
        res.append(num) #append para adicionar o nº à lista
    return res

def somaLista(N):
    global Lista
    soma = 0
    for n in N:
        soma = soma + n
    return soma

def mediaLista(N):
    global Lista
    soma = somaLista(N)
    media = soma / len(N)
    return media 

def maiorLista(N):
    global Lista
    maior = N[0]
    for elem in N[1:]: 
        if elem > maior: 
            maior = elem 
    return maior 

def menorLista(N):
    global Lista
    menor = N[0]
    for elem in N[1:]: 
        if elem < menor: 
            menor = elem 
    return menor 

def OrdenaçãoCresc(N):
    global Lista
    for i in range(len(N) - 1):
        if N[i] > N[i + 1]:
            return "Não"
    return "Sim"

def OrdenaçãoDescres(N):
    global Lista
    for i in range(len(N) - 1):
        if N[i] < N[i + 1]:
            return "Não"
    return "Sim"

def indiceDe(N, elem):
    global Lista
    cond=-1
    if elem in N:
        cond=N.index(elem)+1
    return cond
 
escolha=-1

print("Tens estas opções:\n 1-Criar lista\n 2-Ler lista\n 3-Soma\n 4-Média\n 5-Maior\n 6-Menor\n 7-Ordenada por ordem crescente\n 8-Ordenada por oredem decrescente\n 9-Procura um elemento\n 0-Sair")

while escolha != 0:

    escolha = int(input("Escolhe uma das opções :)"))

    if escolha == 1:
        Lista = CriaLista(int(input("Intoduza o total de números que quer na lista")))
        print(Lista)

    elif escolha == 2:
        Lista = LeLista(int(input("Intoduza o total de números que quer na lista")))
        print(Lista)
        
    elif escolha == 3:
            print("Soma:", somaLista(Lista))

    elif escolha == 4:
        print("Média:", mediaLista(Lista))

    elif escolha == 5:
        print("Maior:", maiorLista(Lista))
    elif escolha == 6:
        print("Menor:", menorLista(Lista))

    elif escolha == 7:
        print("Ordenada por ordem crescente?", OrdenaçãoCresc(Lista))

    elif escolha == 8:
        print("Ordenada por ordem decrescente?", OrdenaçãoDescres(Lista))

    elif escolha == 9:
        print("Lista atual:", Lista)
        num = int(input("Procura um número: "))
        posição = indiceDe(Lista, num)
        if posição == -1:
            print("Número não encontrado.")
        else:
            print(f"Número encontrado na posição {posição}.")
    else:
        print("Escolhes-te a opção de sair :(")
       


