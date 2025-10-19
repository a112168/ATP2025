# %%
# aluno = (nome, id, [notaTPC, notaProj, notaTrste])
# turma = [aluno]
turma = []

def criar_turma():
    turma.clear()
    for i in range(5):
        nome = input("Nome do aluno: ")
        id = input("ID do aluno: ")
        notaTPC = float(input("Nota TPC: "))
        notaProj = float(input("Nota Projeto: "))
        notaTeste = float(input("Nota Teste: "))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
    print("Conseguiste criar a turma!")

def inserir_aluno():
    nome = input("Nome do aluno: ")
    id = input("ID do aluno: ")
    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))
    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    notas = [notaTPC, notaProj, notaTeste]
    turma.append(aluno)
    print("Aluno colocado na turma!")

def listar_turma():
    print("Lista da turma:")
    for aluno in turma:
        print(aluno)

def consultar_por_id():
    id_aluno = input("Insira o ID do aluno: ")
    for  nome, id, notas in turma:
        if id_aluno == id:
            print(f" Aluno encontrado!")
            return
    print("Aluno não encontrado.")

def guardarTurma(turma, fnome):
    file = open(fnome,"w") # abre o ficheiro fnome para escrita
    res="" #string q vai guardar todo o conteudo a escrever
    for a in turma: #percorre cada elemento da lista turma
        nome, id, notas = a 
        res += str(nome) + "-" + str(id) + "-" + str(notas[0]) + "::" + str (notas[1]) + "::" + str(notas[2]) + "|"
        res+="\n"
    file.write(res) #após o loop (file.write) escreve tudo no ficheiro
    file.close()
    
def recuperarTurma(fnome):
    listat = []
    file = open(fnome,"r")
    text=file.read()
    turma_text=text.split("\n")

    for p_text in turma_text[:-1]:
        t=[]
        t_text=p_text.split("|")

        for t_text in t_text[:-1]:
            nome, id, notas = t_text.split("-")

            notas_lista=[]
            for n in notas.split("::"):
                notas_lista.append(float(n))
            alu=(str(nome),str(id),list(notas_lista))
            t.append(alu)
        listat.append(t)
    file.close()
    return listat

# Menu principal
menu = -1
print("""Estas são as opções:
(1)- Criar uma turma;
(2)- Inserir um aluno na turma;
(3)- Listar a turma;
(4)- Consultar um aluno por id;
(5)- Guardar a turma em ficheiro;
(6)- Carregar uma turma dum ficheiro;
(0)- Sair da aplicação""")

while menu != 0:
    menu = int(input("Escolhe a tua opção: "))
    if menu == 0:
        print("Saíste da aplicação!!")
    elif menu == 1:
        criar_turma()
        print(f"A turma é: {turma}")
    elif menu == 2:
        inserir_aluno()
        print(f"O aluno adicionado é: {turma}")
    elif menu == 3:
        listar_turma()
        print(f"A lista da turma é: {turma}")
    elif menu==4:
        consultar_por_id()
    elif menu==5:
        print(f"A sua turma foi guardada no ficheiro: turma")
        guardarTurma(turma,"turma.txt")
    elif menu==6:
        print(recuperarTurma("turma.txt"))
    else:
        print("Tenta escolher um número do menu :)")


