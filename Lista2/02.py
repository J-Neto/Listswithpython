# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
#respectivo vetor. Ao final liste a idade da pessoa mais jovem e a altura da pess.oa mais alta

Age = []
Height = []

for i in range(5):
    Age.append(int(input("Insert the person's age {} : ".format(i + 1))))
    Height.append(float(input("Insert the person's height {} : ".format(i + 1))))

print('The tallest person is {} meter tall'.format(max(Height)))
print('The youngest person is {} years old'.format(min(Age)))