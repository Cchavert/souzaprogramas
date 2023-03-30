divisor = 1

numero = int(input('Informe um número inteiro e positivo: '))
if numero < 0:
    numero = int(input('O número não pode ser negativo.\n Digite um número inteiro e positivo: '))
for divisor in range(divisor, numero):
    if numero % divisor == 0:
        print(divisor)