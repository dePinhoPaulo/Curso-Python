a = 12
b = 12

print(a+b)
#help(print)

#Tipos Basicos
print('\n#Tipos Basicos')

print(True)
print(False)
print("voce " + 2 * "muito ")
print([1, 2, 3])
pessoa = {'nome': 'paulo', 'idade': 22}
print(pessoa)
print(pessoa['nome'])
print(None)

#Variaveis
print('\n#Variaveis')

c = 12
d = 12.5
print(c+d)

c = 'String'
print(c)

#Comentarios

"""
asdasd
asdas
"""

#Operadores Aritimeticos
print('\n#Operadores Aritimeticos')

print(2 + 3)
print(2 - 5)
print(2 * 5.6)
print(9.4/3)
print(9.4//3)
print(2 ** 3)
print(10%3)

e = 12
f = e
print(e+f)

#Desafio Fundamentos
print('\n#Desafio Fundamentos')

#Quantos por cento as Despesas representa do Salario:
salario = 3450.45
despesas = 2456.20

resultado = round((despesas/salario)*100, 2)

print(str(resultado)+"%")

#Operadores Relacionais
print('\n#Operadores Relacionais')

print(2 > 3)
print(2 >= 5)
print(2 < 5.6)
print(9.4 <= 3)
print(9.4 != 3)
print(2 == 2)
print(2 == '2')

#Operadores de Atribuicao
print('\n#Operadores de Atribuicao')

a = 3
a = a + 7
print(a)
a += 5  #a=a+5
print(a)
a -+ 2
print(a)
a *= 2
print(a)
a /= 4
print(a)
a %= 4
print(a)
a **= 8
print(a)
a //= 255
print(a)

#Operadores Logicos
print('\n#Operadores Logicos')

print(True or False)
print(7 != 3 and 2 > 3)

#Tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Tabela verdade do OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Tabela verdade do XOR
print(True != True)
print(True != False)
print(False != True)
print(False != False)

#Tabela de Negação (unario)
print(not True)
print(not False)

#Desafio operadores logicos
#
#

#Operadores Unarios
print('\n#Operadores Unarios')
a = 3
#a ++
print(a)

#Operadores Ternarios
print('\n#Operadores Ternarios')

chovendo = True

print('Roupas estao: ' + ('secas', 'molhadas')[chovendo])

print('Roupas estao: ' + ('molhadas' if chovendo else 'secas'))

#Operadores (Membro/Identidade)
print('\n#Operadores (Membro/Identidade)')

#Membro
lista = [1,2,3,4,'ana','joão']
print(2 in lista)
print('ana' not in lista)

#Identidade
x=3
y=x
z=3
print(x is y)
print(z is y)
print(z is not x)

lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)

#Conversão de tipos
print('\n#Conversao de tipos')
a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

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

#Lista
lista = []
print(type(lista))
print(dir(lista))

print(len(lista))
lista.append(1)
lista.append(5)
lista.append([1,2,3])
print(lista)
print(len(lista))

nova_lista = [1, 5, 'ana', "paulo"]
nova_lista.remove('ana')
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista2 = [1, 5, 'ana', "paulo", 'joao', 3.14]
print(lista2.index('ana'))
print(lista2[1])
print(1 in lista2)
print('pedro' not in lista2) 
print(lista2[0])
print(lista2[-1])
print(lista2[-6])

lista3 = ['ana', "paulo", 'joao', 'maria', 'jose']
print(lista3[1:3])
print(lista3[1:-1])
print(lista3[1:])
print(lista3[:-1])
print(lista3[::2])
print(lista3[::-1])
del lista3[2]
print(lista3)
del lista3[1:]
print(lista3)

#Tuplas
tupla = tuple()
tupla = ()
print(type(tupla))
print(dir(tupla))
print(help(tuple))

tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))

print(tupla[0])
#tupla[0] = 'dois' #tupla não pode ser mudada
print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'azul', 'azul')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))

#Dicionarios
pessoa = {'nome': 'ana', 'idade': 38, 'cursos': ['espanhol', 'ingles']}
print(type(pessoa))
print(len(pessoa))

print(pessoa['nome'])
print(pessoa['cursos'][1])
#print(pessoa['tags'])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', [])) #seta valor defult para retornar

pessoa = {'nome': 'joao', 'idade': 38, 'cursos': ['python', 'java']}
pessoa['idade'] = 44
pessoa['cursos'].append('c#')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({'idade': 40, 'sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)

#Conjuntos
a = {1, 2, 3}
print(type(a))
#print(a[0])
a = set('coddder')
print(a)
print('3' in a, 4 not in a)
{1,2,3} == {3,2,1,3}

c1 = {1,2}
c2 = {2,3}

print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)
print(c2 <= c1)
print(c1 >= c2)

print({1,2,3} - {2})
print(c1-c2)
c1 -= {2}
print(c1)

#Interpolação
from string import Template
nome, idade = 'ana', 23

print('Nome: %s, Idade: %i' %(nome, idade)) #mais antiga
print('Nome: {0}, Idade: {1}'.format(nome, idade)) #python < 3.6
print(f'Nome: {nome}, Idade: {idade}') #python >= 3.6

s = Template('Nome: $nome, Idade: $idade')
print(s.substitute(nome=nome, idade=idade))