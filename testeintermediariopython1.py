a=10
b=00
try:
    print(a/b)
    
except ZeroDivisionError as error:
    
    print("Não pode Dividir por 0",error)