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