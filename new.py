#coerção automatica

print(type(10/2))

print(type(10//3))

print(type(2+True))
print(type(2+1.3))

#Tipos numeriocos

print(dir(int))
print(dir(float))

a = 5
b = 2.5
print(a/b)
print(a+b)
print(a*b)
print(a-b)

print(b.is_integer())
print((5.0).is_integer())

print(int.__add__(2,3))

print((-2).__abs__())
print((-2.5).__abs__())

print(1.1 + 2.2)
from decimal import Decimal, getcontext
print(Decimal(1)/Decimal(7))

getcontext().prec = 4
print(Decimal(1)/Decimal(7))
print(Decimal.max(Decimal(1),Decimal(7)))

print(dir(Decimal))

print(Decimal(1.1)+Decimal(2.2))

import decimal
print(dir(decimal))

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