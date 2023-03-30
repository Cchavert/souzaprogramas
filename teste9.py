n1 = int(input("Digite um numeo: "))
maior = n1
menor = n1
n2 = int(input("Digite um numeo: "))
if n2 > maior:
    maior = n2
else:
     menor = n2
n3 = int(input("Digite um numeo: "))
if n3 > maior:
    maior = n3
else:
    if n3 < menor:
        menor = n3
print(f"maior {maior}")
print(f"menor {menor}")