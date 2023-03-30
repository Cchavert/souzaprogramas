arquivo=open("numeros.text","a")
#for i in range(1,101):
nome=input("Informe seu Nome: ")
email=input("Informe seu E-mail: ")
arquivo.write(f" Nome: {nome} e Contato: {email}")
arquivo.close()