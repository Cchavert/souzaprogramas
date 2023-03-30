#Dicionario 
comida ={"Alface": 0.45, "Milho": 1.00}
valor = input("Informe o nome da Comida:  ")
if valor in comida:
    print(comida[valor])
else:
    print("Item não Encontrado: ")