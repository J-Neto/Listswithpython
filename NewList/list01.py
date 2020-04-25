'''
01. Faça um algoritmo que leia 2 vetores numéricos A[10] e B[10]. A seguir, crie um vetor C que seja a intersecção de A com B e mostre
este vetor C. Obs.: intersecção é quando um valor estiver nos dois vetores. Considere que não há elementos duplicados em cada um
dos vetores.
'''
from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(int(input(f"Digite o número na primeira linha, posição {i}: ")))
    b.append(int(input(f"Digite o número na segunda linha, posição {i}: ")))   

for i in range(len(a)):
    for j in range(len(b)):
        if(b[j] == a[i]):
            c.append(b[j])

print(a)
print(b)
print(c)