# DESAFIO PYTHON
# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58

#Funcionamento: Haverá um menu de controle para que o Usuário escolha o que deseja realizar
#1 para calcular, 2 para sair. Caso escolha uma opção inexistente, o programa avisa.

#José Ribeiro Neto

#Variável de controle
exit = False
print('Cálculo do Peso Ideal')

#Loop do menu
while(exit == False):
    op = int(input(('1- Calcular peso\n2- Sair do programa\nOpção: ')))
    
    if(op == 1):
        altura = float(input('Insira a sua altura: '))
        peso = (72.7 * altura) - 58
        print('O seu peso ideal é: {:.2f}'.format(peso))

    elif(op == 2):
        exit = True

    else:
        print('ERRO! Insira uma opção válida!')