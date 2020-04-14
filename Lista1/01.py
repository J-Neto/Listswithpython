#Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

import random as r

#Define list length
listX = [0] * 10
print(listX)
cont = 0

#Generating random list
for i in range(len(listX)):
    rand_number = r.randint(0,100)
    listX[i] = rand_number

for i in range(len(listX)):    
    if((listX[i] % 2) == 0):
        cont = cont+1

print(listX)
print(cont)