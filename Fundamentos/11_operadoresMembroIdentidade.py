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