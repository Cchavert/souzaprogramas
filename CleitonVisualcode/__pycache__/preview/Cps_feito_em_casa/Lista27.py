# List Comprehension foi concebida na PEP 202 e é uma forma concisa de criar e manipular listas. Sua sintaxe básica é a seguinte:
#[expr for item in lista] Ou seja, aplica a expressão expr em cada item da lista. 
# Exemplo 1: elevar os elementos da lista ao quadrado (à 2ªpotência) utilizando for:


lista = [item**2 for item in range(10)] #Podemos reescrevê-lo, utilizando List Comprehensions, da seguinte forma:

for item in range(10):
    
    lista.append(item**2)
    
    print(lista)