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