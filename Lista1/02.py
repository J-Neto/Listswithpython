import random as r

#Define list length
listX = [0] * 15
print(listX)

#Adicionar notas
for i in range(len(listX)):
    nota1 = float(input("Digite a nota do primeiro aluno: "))
    listX[i] = nota1
print(listX)

media = sum(listX)/15
print(media)
print(listX)