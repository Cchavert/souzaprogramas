#Except
#try
entrada=input("Digite um número: ")
try:
    numero=int(entrada)
    print("O numero digita foi: ",numero)
except ValueError:
    print("oops! Voçe não digitou nem um número válido. tente novamente.")