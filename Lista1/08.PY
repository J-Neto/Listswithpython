#Faça um programa que receba do usuário dois vetores, A e B, com 10 números
#inteiros cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os
#dados do vetor C
import random as r

A = [0] * 10
B = [0] * 10
C = []

for i in range(10):
    random_number = r.randint(0, 100)
    A[i] = random_number

for i in range(10):
    random_number = r.randint(0, 100)
    B[i] = random_number

for i in range(10):
    C.append(A[i] - B[i])
    
print('A: {}'.format(A))
print('B: {}'.format(B))
print('C: {}'.format(C))