# CASO 1: Detectar CPF duplicado em cadastro
cpfs = ['123.456.789-00', '987.654.321-00', '123.456.789-00', '111.111.111.11']

unicos = set (cpfs)
duplicaos = len(cpfs) - len(unicos)
print(f'Total cadastrado: {len(cpfs)}')
print(f'CPFs únicos: {len(unicos)}')
print(f'Duplicados: {duplicados}')

# CASO 2: Coordenadas GPS - tuplas garante que ninguém muda a posição

SENAI_SIG = (-15.8311, -48.0500) # Constante
lat, lon = SENAI_SIG
print('SENAI está em: {lat}, {lon} ')


# CASO 3: Função que retorna múltiplos valores
def estatisticas(notas):
# Retorna média, maior e menor nota como tupla 
     return sum(notas)/len(notas), max(notas), min(notas)
media, maior, menor = estatisticas([8.5, 7.0, 9.2, 6.5])
print(f'Média: {media:.2f} Maior: {maior:.2f} Menor: {menor:.2f}')
   
