#Escreva um programa para ler um vetor A de 10 elementos inteiros
#e um valor X. A seguir imprimir "ACHEI" se o valor X existir em A e "NÃO ACHEI" caso
#contrário.

import random as r

A = [0] * 10
X = random_number = r.randint(0, 5)
achou = 0

for i in range(10):
    random_number = r.randint(0, 5)
    A[i] = random_number

for i in range(len(A)):
    if (A[i] == X):
        achou = 1

print('Vetor {}'.format(A))
print('Número {}'.format(X))
if(achou == 1):
    print('ACHEI')
else:
    print('NÃO ACHEI')