#Strings 
print(dir(str))

nome = 'Sao Paulo'
nome
print(nome[0])
#print(nome[0]='p')

"maria d'vila" == 'maria d\'vila'
print("teste \"escape")
texto = 'texto entre apostrofos pode ter "aspas"'
print(texto)

doc = """txto com multiplas
...linhas
"""
print(doc)

nome1 = 'Ana Paula'
print(nome1[1])
print(nome1[6])
print(nome1[-2]) 
print(nome1[4:]) 
print(nome1[:4]) 
print(nome1[2:5]) 
print(nome1[::-1]) 

numeros = '1234567890'
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])

frase = 'Python e uma linguagem excelente'
print('py' not in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())
frase = frase.upper()

print(frase.split())
print(frase.split('E'))

print(dir(str))
print(help(str.center))

a = '123'
b = ' de oliveira 4'
print(a+b)
print(a.__add__(b))
print(str.__add__(a, b))

print(len(a))
print(a.__len__())

print('1' in a)
print(a.__contains__('1'))

print(dir(str))
print(help(str.__gt__))