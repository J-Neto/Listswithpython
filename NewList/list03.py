secreta = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", 
"j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
"u", "v", "w", "x", "y", "z"]

frase = [2,15,13,0,4,9,1]
novafrase = []

for i in range(len(frase)):
    novafrase.append(secreta[frase[i]])

print(novafrase)