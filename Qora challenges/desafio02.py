# DESAFIO CONDICIONAIS
# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
# conforme o caso.

#José Ribeiro Neto
#Ele usa upper para caso o usuário digite minúsculo

op = str(input('Em qual turno você estuda?\nM- Matutino\nV- Vespertino\nN- Noturno\n').upper())
if(op == 'M'):
    print('Bom Dia!')
elif(op == 'V'):
    print('Boa Tarde!')
elif(op == 'N'):
    print('Boa Noite!')
else:
    print('Valor inválido')