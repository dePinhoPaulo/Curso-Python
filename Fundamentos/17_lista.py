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
