#Escreva um programa para ler um vetor A de 10 elementos inteiros e um valor X. A
#seguir imprimir os índices do vetor A em que aparece um valor igual a X.

import random as r

A = [0] * 10
X = random_number = r.randint(0, 5)
indices = []

for i in range(10):
    random_number = r.randint(0, 5)
    A[i] = random_number

for i in range(len(A)):
    if (A[i] == X):
        indices.append(i)

print('Vetor {}'.format(A))
print('Número {}'.format(X))
print('Índices {}'.format(indices))