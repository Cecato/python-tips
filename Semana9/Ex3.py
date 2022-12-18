import random
import time
import os
import names

to = time.time()

random.seed(42)

qtde_nomes_unicos = 3000
qtde_nomes_aleatorios = 10000000

print("--> Criando conjunto de dados com {} nomes".format(qtde_nomes_aleatorios))
print("--> Esse processo pode demorar mais de {} segundos".format(180))

aux = []

for i in range(0, qtde_nomes_unicos):
    aux.append(names.get_full_name())

print("--> Gerando {} nomes aleatorios". format(qtde_nomes_aleatorios))
dados = []

for i in range(0, qtde_nomes_aleatorios):
    dados.append(random.choice(aux))
    
type(dados)
print(dados[0])
print(dados[1])
print(dados[2])

print("--> Gravando em arquivo.")

arquivo = open('nomes_aleatorios.txt','w')

for item in dados:
    arquivo.write(item+'\n')
    
arquivo.close()

tf = time.time() - to
print("--> Criacao Finalizando em {} segundos".format(tf))