#arquivo=open("numeros.text","w")
#for i in range(1,101):
   #arquivo.write("%d\n"% i)
#arquivo.close()




arq = open("arquivoler.txt","r")
for n in arq.readlines():
   print(n) 
arq.close()