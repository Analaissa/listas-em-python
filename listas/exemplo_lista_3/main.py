alunos = ['Carlos','Ana','Diana','Bruno']

# append, insert, remove, pop
alunos.append('Eduardo') # append insere ao final
alunos.insert(0,'Alice') # insert eu escolho a posição
alunos.remove('Diana') 
ultimo = alunos.pop()
print(alunos,'| removido:', ultimo)

# sort vs sorted
alunos.sort() # modifica no lugar
nova = sorted(alunos, reverse=True) # cria nova lista
print(alunos, nova)

# in, index, count
print('Ana' in alunos) # verifica se Ana existe na lista
print(alunos.index('Ana')) # mostra o indice do nome Ana
