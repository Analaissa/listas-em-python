# Lista de tuplas
produtos = [
    (1001, "Notebook", 24, 18),
    (1002, "Mouse", 12, 14),
    (1003, "Monitor", 36, 10),
    (1004, "Teclado", 12, 12),
    (1005, "Impressora", 18, 20)
]

em_garantia = 0
vencidos = 0

print("Código\tNome\t\tGarantia\tUso")

for produtos in produtos:
    codigo, nome, garantia, uso = produtos

    if uso<= garantia:
        restante = garantia - uso 
    print(f"{codigo}\t{nome}\t\t{garantia} meses\t{uso}m\tEm garantia ({restante} meses restantes)")
    em_garantia +=1 
    else:
    vencido = uso - garantia
    print(f"{codigo}\t{nome}\t\t{garantia} meses\t{uso}m\tGarantia vencida ({vencido} meses atrás)")
    vencidos +=1
    print("\n=== Resumo ===")
    print(f"Total: {len(produtos)}")
    print(f"Em garantia: {em_garantia}")
    print(f"Vencidos: {vencidos}")