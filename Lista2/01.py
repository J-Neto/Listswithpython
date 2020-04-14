#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números
#pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 

import random as r
A = []
B = []
#Define list length
listX = [0] * 20

#Generating random list
for i in range(len(listX)):
    rand_number = r.randint(0,20)
    listX[i] = rand_number

print(listX)
for i in range(len(listX)):
    if (listX[i] % 2) == 0:
        A.append(listX[i])
    else:
        B.append(listX[i])

print(A)
print(B)