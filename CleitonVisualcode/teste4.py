minutos = int(input(" Quantos minutos voçe utilizou este Mês:"))
if minutos < 200:
    preço = 0.20
else:
        if minutos < 400:
            preço = 0.18
        else:
          preço = 0.15    
    


print(f'Voçe vai pagar este mês: { minutos * preço} ')

