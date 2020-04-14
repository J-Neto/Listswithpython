#Escreva um programa em para ler um vetor X de 10 elementos inteiros. Logo após
#copie os elementos do vetor X para um vetor Y fazendo com que o 1o. elemento de X
#seja copiado para o 10o. De Y, o 2o. de X para o 9o. de Y e assim sucessivamente.
#Após o término da cópia, imprimir o vetor Y.

import random as r

X = []
Y = [0] * 10

for i in range(10):
    random_number = r.randint(0, 100)
    X.append(random_number)

j = 9
for i in range(10):
    Y[j] = X[i]
    if(j != 0):
        j = j-1

print(X)
print(Y)