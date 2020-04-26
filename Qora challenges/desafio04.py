# DESAFIO FUNÇÕES
# Reverso do número. Faça uma função que retorne o 
# reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.

def reverso(x):
    print(x[::-1]) 

num = input('insira qualquer número: ')
reverso(num)