# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contraram para desenvolver o programa que calculará os reajustes.
#• Faça um programa que recebe o salário de 15 colaboradores e o reajuste segundo o seguinte
#critério, baseado no salário atual:
#• salários até R$ 280,00 (incluindo) : aumento de 20%
#• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#• salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
#• o salário de cada colaborador antes do reajuste;
#• o novo salário de cada colaborador, após o aumento.
#• informe o maior salário entre os colaboradores

import random as r

salary = []
new_salary = [0] * 5

for i in range(len(new_salary)):
    random_number = r.randint(100,3000)
    salary.append(random_number)

salary.sort()

for i in range(len(new_salary)):
    if((salary[i] >= 0) & (salary[i] <= 280)):
        new_salary[i] = salary[i] + (salary[i] * 0.2)

    elif((salary[i] >= 280) & (salary[i] <= 700)):
        new_salary[i] = salary[i] + (salary[i] * 0.15)

    elif((salary[i] >= 700) & (salary[i] <= 1500)):
        new_salary[i] = salary[i] + (salary[i] * 0.1)

    elif(salary[i] >= 1500):
        new_salary[i] = salary[i] + (salary[i] * 0.05)

print('Salário antes do reajuste: {}'.format(salary))
print('Salário após do reajuste: {}'.format(new_salary))
print('O maior salário dentre os colaboladores é: {}'.format(max(new_salary)))