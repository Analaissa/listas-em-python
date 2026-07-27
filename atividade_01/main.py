# lista com as temperaturas da semana
temperaturas = [28.5, 31.0, 25.5, 33.22, 29.8, 27.1]
#Calculando média, maior e menor temperatura
media = sum(temperaturas)/ len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

# Contando qunatos dias ficaram acima da média
dias_acima = 0
for temperatura in temperaturas:
    if temperatura > media:
        dias_acima += 1

#criando uma lista em ordem cresceste sem alterar a original
temperaturas_ordenadas = sorted(temperaturas)

# Exibindo o relatório
print("temperaturas registradas:", temperaturas)

print("\n====== relatório climático ======")
print(f"média:  {media:.2f} °C")
print(f"máxima: {maxima:.2f}°C")
print(f"mínima: {minima:.2f}°C")
print(f"Dias acima da média: {dias_acima}")
print("Em ordem crescente:", temperaturas_ordenadas)