'''
2 - Dados dois vetores, um contendo a quantidade e o outro o preço de 20 produtos, elabore um algoritmo que calcule e exiba o
faturamento que é igual a quantidade x preço. Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos,
a média dos faturamentos e quantos faturamentos estão abaixo da média. 
'''
#Importing randint
from random import randint
from numpy import mean

quantidade = []
preco = []
faturamento = []
cont = 0

for i in range(20):
    #Generating random int
    quantidade.append(randint(1,10))
    preco.append(randint(1,10))

    #Multiplication
    faturamento.append(quantidade[i] * preco[i])

total_faturamento = sum(faturamento)
media_faturamento = mean(faturamento)

for i in range(20):
    if(faturamento[i] < media_faturamento):
        cont = cont + 1

print('O faturamento é igual a {}'.format(total_faturamento))
print('A média do faturamento é igual a {}'.format(media_faturamento))
print('Existem {} faturamentos abaixo da média'.format(cont))