# %% [markdown]
# # Aula Prática 7 (guião)
# ### Semana de 27 a 31 de Outubro de 2025
# ### José Carlos Ramalho e Luís Cunha
# ### Sinopsis:
# 
# * Consolidação e aferição de tudo o que foi feito até ao momento. 
# 
# ---

# %% [markdown]
# ### Assunto: Frações
# Vamos pensar num modelo: o que é uma fração estruturalmente?

# %%
# Fração = (numerador, denominador)
# numerador = Int
# denominador = Int
# Modelo duma fração
f1 = (1,3)  # 1/3

# Modelo duma lista de frações
lf1 = [(1,2),(1,3),(1,4)] # 1/2, 1/3, 1/4

# %% [markdown]
# ### Construtor

# %%
def criarFracao(numerador, denominador):
    return (numerador, denominador)

def verFracao(f):
    # numerador = f[0]
    # denominador = f[1]
    numerador, denominador = f
    print(f"{numerador}/{denominador}")
    return

verFracao(f1)

# %%
f1 = criarFracao(2,3)
verFracao(f1)

# %% [markdown]
# ### Simplificação de frações

# %% [markdown]
# Divisão
# 
# a=42 e b=30
# 
#     a%b     resto    a=b    b=r
# 1º  42%30    12      a=30   b=12
# 2º  30%12     6      a=12   b=6
# 3º  12%6      0

# %%
# 1 - dividir o maior número (a) pelo menor (b) e registar o resto (r)
# 2 - se r != 0 substituir o número (a) por (b) e substituir o (b) por (r)
# 3 - repetir as etapas anteriores até que (r) == 0. Nesse momento o número (b) corresponde ao mdc (máximo divisor comum)

#O teu programa serve para simplificar uma fração.
#Por exemplo, transformar 55/80 em 11/16.
#Para isso, ele precisa descobrir o maior número que divide os dois — o chamado mdc-..............................................

#Passo 1 → garante que o maior vem primeiro → ficamos com (80, 55).
#Passo 2 → faz 80 ÷ 55 → resto = 25
#Agora, calcula MDC(55, 25)
#Passo 3 → 55 ÷ 25 → resto = 5
#Agora, calcula MDC(25, 5)
#Passo 4 → 25 ÷ 5 → resto = 0
#Quando o resto dá 0, o MDC é o último divisor, neste caso 5.
#Portanto: MDC(55, 80) = 5

# stor fez
def mdc (a,b): #método iterativo
    if a < b: #Se a for menor que b, troca as posições (para dividir sempre o maior pelo menor).
        a, b = b, a #fica (b,a)
    while a % b != 0: #Enquanto o resto for diferente de 0, o ciclo continua.
        r = a % b #resto
        a=b
        b=r 
    return b #quando o resto é 0, b é o mdc

# funçao recursiva: é uma função que se chama a si própria para resolver um problema mais pequeno até chegar a um caso simples, que se chama caso base.
#Pensa nisto como subir uma escada:
#Cada chamada recursiva é um degrau — a função vai subindo até encontrar o “fim” (o caso base), e depois volta com a resposta.
def mdc_rec(a,b):
    if a% b == 0: #se o resto de a/b = 0, quer dizer que b divide exatamente a, então é o mdc
        return b
    #se n for 0-> ainda n encontramos o mdc, então chamamos de novo a função mdc_rec
    #mas trocando os papeís, agr a=b antigo e b=resto (a%b), isto ocorre até o resto=0
    return mdc_rec(b,a%b)

def simplificarFracao(f):
    m = mdc(f[0], f[1]) #f0 numerador, f1 denominador
    return(f[0]/m, f[1]/m)

print(simplificarFracao((55, 80)))

# %%
# eclipse e xixa fizeram
def mdc (a,b): #falta a opção de trocar o a pelo b caso o a seja menor 
    divisao = a%b
    while divisao != 0:
        divisao = a%b
        a=b
        b=divisao
    return a
# problema ---> não da caso o b seja o proprio mdc?????

def simplificarFracao(f):
    numerador, denominador = f
    d = mdc(numerador, denominador)
    # tuplo = (numerador/a, denominador/a)
    return (numerador/d, denominador/d)


# %%
verFracao(simplificarFracao(criarFracao(21, 140)))

# %% [markdown]
# ### Frações equivalentes
# 
# Defina uma função que recebe duas frações como argumento e devolve `True` se as frações são equivalentes e `False` caso contrário.

# %%
def equivalenteFracao(f1,f2):
    return simplificarFracao(f1) == simplificarFracao(f2)
            #uma tupla                 outra tupla
            #em python == para tuplas compara elemento a elemento, se todos forem = resultado é true
equivalenteFracao((1,2), (14,28))

# %% [markdown]
# ## Operações sobre frações

# %%
def somarFrac(f1, f2):
    return (f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1])
          #a/b + c/d =     axd + cxb      /  bxd

f1 = criarFracao(15, 21)
f2 = criarFracao(5,7)
verFracao(somarFrac(f1,f2))
verFracao(somarFrac((1,2),(1,2)))

# %%
listaFrac = [f1, f2, criarFracao(125,1000), (8,12)]
# f1 e f2 vai buscar os valores de cima
listaFrac2 = []
import random
for i in range(1,20): # repete 20 vezes
    n = random.randrange(1, 10) #nª aleatório entre 1 e 9
    d = random.randrange(2, 20) #entre 2 e 19
    listaFrac2.append(criarFracao(n,d))
print(listaFrac2) #vamos ter 20 frações aleatórias

# %% [markdown]
# ### Soma uma lista de frações

# %%
def somarListaFrac(lista):
#somará todas as frações da lista e devolve uma única fração
    soma = lista[0] #começar com a 1ª fração
    for f in lista[1:]: #soma todas as outras
        soma = somarFrac(soma,f) #função usada em cima para somar funções
#pegamos na próxima fração da lista para somar com a fração soma que obtivemos e repetimos até à última
    return simplificarFracao(soma) #para simplificarmos a função final

verFracao(somarListaFrac(listaFrac))
verFracao(somarListaFrac(listaFrac2))

# %% [markdown]
# ### Multiplica 2 frações

# %%
def multFrac(f1, f2):
    multi = (f1[0] * f2[0], f1[1] * f2[1])

    return simplificarFracao(multi)

f1 = criarFracao(15, 21)
f2 = criarFracao(5,7)
verFracao(multFrac(f1,f2))

# %% [markdown]
# ### Ordenar uma lista de frações por ordem decrescente

# %% [markdown]
# diferenças entre sort e sorted
# 
# NÃO FAZER
# listaA[1,7,5,2]
# listaB = listaA.sort()
# print(listaB)
# (None ---> não dá nada) 
# 
# O CORRETO É:
# listaA[1,7,5,2]
# listaB = sorted(listaA) ---> dá a lista B (lista A ordenada)
# 
# listaA.sort() ---> dá a lista A ordenada

# %%
#!!!!python nao consegue organizar as frações, só vê o primeiro elem do tuplo
listaA = [(2,2), (1,3), (9,100000)]
listaB = sorted(listaA) #dá uma lista b que é a lista A ordenada só tendo em conta o priemiro número de cada
print(listaB)

# %%
#RESOLUÇÃO CERTA
def ordena_frac(elem): #elem é uma fração da lista
    return elem[0]/ elem[1] #converte fração em nº decimal
    #elem0- numerador, elem1-denominador
def ordenaFracDec(lista):
    x = sorted(lista, key=ordena_frac, reverse=True) # ordem crescente
    #sorted-função que ordena a lista
    #key=...-para cada fração ele chama oredena_fração(fração) e usa o valor decimal para ordenar a lista
    #reverse=true - significa ordem decrescente
    #x guarda a lista já ordenada
    return x

print(ordenaFracDec(listaFrac))

# %% [markdown]
# ### Guardar uma lista de frações num ficheiro

# %%
import json
def gravaListaFrac(fnome, lista):
#fnome-nome do ficheiro ond evamos guardar a lista
    file=open(fnome,"w") #abre um ficheiro com aquele nome para escrever
    #!!!Se o ficheiro não existir, Python cria um ficheiro novo.
    #Se já existir, Python apaga o conteúdo antigo e escreve de novo
    json.dump(lista,file)
#json é uma biblioteca que converte objetos Python (como listas e tuplas) 
#em texto que pode ser guardado no disco.

#json não guarda tuplas, então (15,21) é convertido para [15,21] no ficheiro.
    file.close

# %%
gravaListaFrac("fracoes.json", listaFrac)

# %% [markdown]
# ### Recuperar uma lista de frações dum ficheiro

# %%
def carregaListaFrac(fnome):
#Objetivo: abrir o ficheiro, ler a lista que lá está e devolver essa lista para o Python.
    file=open(fnome) #abrir o ficheiro para o programa poder ler o conteúdp
    res=json.load(file)
#lê o conteúdo do ficheiro em formato JSON e converte para objetos Python.
#!!!!Lembra que as tuplas foram convertidas em listas quando guardámos o ficheiro.
#Então o resultado são listas, não tuplas!!!!
    return res

# %%
listaAula = carregaListaFrac("fracoes.txt")
print(listaAula)

# %% [markdown]
# ---
# 
# ## TPC7: Teste de aferição
# 
# Resolva os problemas apresentados a seguir.

# %% [markdown]
# ### tpc-1. Especifique as seguintes listas em compreensão:

# %% [markdown]
# #### a) Lista formada pelos elementos que não são comuns às duas listas:

# %%
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns=[]
for x in lista1: #ver os da lista 1 que não estão na lista 2
    if x not in lista2:
        ncomuns.append(x)
for x in lista2:  #ver os da lista 2 que não estão em lista 1
    if x not in lista1:
        ncomuns.append(x)

print(ncomuns)
# Resultado esperado: [1,2,3,7,8]

# %% [markdown]
# #### b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

# %%
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
palavras = texto.split() #para quebrar o texto em palavras usando o espaço como separador
lista=[]
for palavra in palavras:
    if len(palavra)>3:  #len pq queremos palavras com mais de 3 caracteres, comprimento da palavra > 3
        lista.append(palavra)
print(lista)

# Resultado esperado: ['Vivia', 'poucos', 'anos', 'algures', 'concelho', ...]

# %% [markdown]
# #### c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:

# %%
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listares=[]
indice=1 
for palavra in lista: #para cada palavra no tuplo
    tuplo= (indice, palavra) 
    listares.append(tuplo) 
    indice= indice + 1 #indice+=1 para avançarmos no índice 
print(listares)
# Resultado esperado: [(1,'anaconda'), (2,'burro'), (3,'cavalo'), (4,'macaco')]

# %% [markdown]
# ### tpc-2. À semelhança do que foi feito nas aulas, realize as seguintes tarefas:

# %% [markdown]
# #### a) Especifique uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:

# %%
def strCount(s, subs):
    cont=0
    i=0
    while i<len(s):
        pedaco=s[i:i+len(subs)]
        if pedaco==subs:
            cont+=1
            i+=len(subs)
        else:
            i+=1

    return cont
   


#n percebiiiiiiiiiiii

strCount("catcowcat", "cat") # --> 2
strCount("catcowcat", "cow") # --> 1
strCount("catcowcat", "dog") # --> 0

# %% [markdown]
# #### b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:

# %%
def produtoM3(lista):
    menor1, menor2, menor3 = sorted(lista[:3]) #inicia no 0 e para no 2
   #inicia os 3 menores com os 3 primeiros
    for n in lista[3:]: #percorre o resto da lista(dps desses3)
        if n<menor1:
            menor3=menor2
            menor2=menor1
            menor1=n 
        elif n<menor2: #passamos para aqui caso o n seja maior que o menor1
            menor3=menor2
            menor2=n
        elif n<menor3: 
            menor3=n

    return menor1*menor2*menor3


    
print(produtoM3([12,3,7,10,12,8,9]))
# Resultado esperado: 168 = 3 * 7 * 8

# %% [markdown]
# #### c) Especifique uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:

# %%
# Input: 38
# Output: 2
# Explicação: 3 + 8 = 11, 1 + 1 = 2.

# Input: 777
# Output: 3
# Explicação: 7 + 7 + 7 = 21, 2 + 1 = 3.

def reduxInt(n):
    while n >= 10: #para ter mais do que 2 dígitos
        soma=0
        for digito in str(n):
            soma = soma + int(digito)
        n = soma
    return n

numero= int(input("Digite um nº inteiro positivo"))

resultado = reduxInt(numero)
print("O digito final é:", resultado)
#VER ESTE

    

# %% [markdown]
# #### d) Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:

# %%
# Invocação: indexOf("Hoje está um belo dia de sol!", "belo")
# Resultado: 13

# Invocação: indexOf("Hoje está um belo dia de sol!", "chuva")
# Resultado: -1

def myIndexOf(s1, s2):  #s1 frase, s2 palavra
    palavras = s1.split()
    i=0
    encontrou=True #para saber se encontrou ou não
    for palavra in palavras:
        if palavra == s2:
            print("A palavra está no índice:", i)
            encontrou=True
        i=i+1
    if not encontrou:
        print("-1")
    


s1= str(input("Digite uma frase:"))
s2= str(input("Digite uma palavra que quer procurar na frase:"))

myIndexOf(s1,s2)

# %% [markdown]
# ### tpc-3. A Rede Social
# 
# Considere que a informação sobre uma rede social está armazenada numa lista de dicionários.
# 
# Cada dicionário, correspondente a um _post_ e tem chaves `id`, `conteudo`, `autor`, `dataCriacao` e `comentarios`.
# Por sua vez, `comentarios` é uma lista de dicionários com chaves `comentario` e `autor`.
# 
# Considere o seguinte exemplo:
# 
# ``` 
#     MyFaceBook = [{
#         'id': 'p1', 
#         'conteudo': 'A tarefa de avaliação é talvez a mais ingrata das tarefas que um professor
#     tem de realizar...', 
#         'autor': 'jcr', 
#         'dataCriacao': '2023-07-20', 
#         'comentarios': [
#             {
#                 'comentario': 'Completamente de acordo...',
#                 'autor': 'prh'
#             },
#             {
#                 'comentario': 'Mas há quem goste...',
#                 'autor': 'jj'
#             }
#         ]},
#         {
#             'id': 'p2',
#             ...
#         },
#         ...
#         ]
# ```

# %% [markdown]
# Defina as seguintes funções de manipulação e consulta da rede social:

# %% [markdown]
# #### a) `quantosPost`, que indica quantos posts estão registados:

# %%
def quantosPost(redeSocial):
    res=0
    for i in redeSocial:
        res+=1
    return res
    

# %% [markdown]
# #### b)  `postsAutor`, que devolve a lista de posts de um determinado autor:

# %%
def postsAutor(redeSocial, autor):
    p=[]
    for post in redeSocial:
        if post['autor']==autor:
            p.append(post)
            
    return p

# %% [markdown]
# #### c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:

# %%
def autores(redeSocial):
    a=[]
    for post in redeSocial:
        if post['autor'] not in a:
            a.append(post['autor'])
    b=sorted(a) 
    return b

# %% [markdown]
# #### d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social. 
#     
# O campo `id` devrá ser calculado a partir dos já existentes, por exemplo, se a rede tiver posts com id `p1`, `p2` e `p3`, o novo `id` deverá ser `p4`.

# %%
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    res=len(redeSocial)
    i=f'p{res+1}'
    post={
        'id':i,
        'conteudo':conteudo,
        'autor':autor,
        'dataCriacao':dataCriacao,
        'comentarios':comentarios
    }
    redeSocial.append(post)
    return redeSocial

# %% [markdown]
# #### e)  `remPost`, que remove um post da rede, correspondente ao `id` recebido.

# %%
def remPost(redeSocial, id):
    novaRedeSocial=[post for post in redeSocial if post['id']!=id]
    return novaRedeSocial

# %% [markdown]
# #### f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).

# %%
def postsPorAutor(redeSocial):
    cont=0
    rede={}
    for i in redeSocial:
        autor = i['autor']
        if autor in rede:
            rede[autor]+=1
        else:
            rede[autor]=1
    return rede

# %% [markdown]
# #### g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

# %%
def comentadoPor(redeSocial, autor):
    res=[]
    for post in redeSocial:
        for comentario in post:
            if autor==comentario['autor']:
                res.append(post['comentarios'])
    return res


