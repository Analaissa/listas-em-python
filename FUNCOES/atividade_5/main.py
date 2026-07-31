def validar_cpf (cpf):
    if len(cpf) != 11:
        return False
     
    if len(set(cpf)) == 1:
        return False
    return True

cpf = input('Digite o CPF (somente número,' 'sem pontos e traço):').strip()

if len(cpf) == 11:
   print(f'CPF inválido: deve ter 11 digitos (encotrados: {len(cpf)})') 
elif len(set(cpf)) == 1:
    print('CPF inválido: todos os digitos são iguais.')
else:
      print(f'CPF {cpf} - válido (formato correto).')