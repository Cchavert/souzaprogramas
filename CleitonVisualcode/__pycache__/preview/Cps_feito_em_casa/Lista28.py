# LIST COMPREHENSIONS COM “IF” As estruturas em List comprehensions podem utilizar 
# expressões condicionais para criar listas ou modificar listas existentes. Sua sintaxe básica é:

[expr for item in lista if cond]

resultado = [numero for numero in range(20) if numero % 2 == 0]