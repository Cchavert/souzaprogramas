#Com a função enumerate() podemos percorrer também o índice referente a cada valor da lista:
lista = [10, 20, 30, 40, 50, 60]
for indice, valor in enumerate(lista):
    print(f'índice={indice}, valor={valor}')