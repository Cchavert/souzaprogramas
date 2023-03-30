# No primeiro loop, i assume o valor de 0, portanto [linha[0] for linha in matriz] vai retornar o primeiro elemento de cada linha: [1, 4, 9]
# No segundo loop, i assume o valor de 1, portanto [linha[1] for linha in matriz] vai retornar o segundo elemento de cada linha: [2, 5, 10]
# No terceiro loop, i assume o valor de 2, portanto [linha[2] for linha in matriz] vai retornar o terceiro elemento de  cada linha: [3, 6, 11]
# No quarto loop, i assume o valor de 3, portanto [linha[3] for linha in matriz] vai retornar o quarto elemento de cada linha: [4, 8, 12]

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

transposta = [[linha[i] for linha in matriz] for i in range(4)] 

print(transposta)
