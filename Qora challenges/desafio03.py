# DESAFIO REPETIÇÃO
# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# qual numero voce deseja receber a sequencia fibonacci? 34

#José Ribeiro Neto

num = int(input('Qual número você deseja receber a sequência fibonacci?'))
#Valor a ser somado
ant = 0
#Valor de referência
atual = 1
#Valor intermediário que salva o valor anterior antes de ser alterado
inter = 0

while(atual <= num):
    print(atual)
    inter = atual
    atual = atual + ant
    ant = inter