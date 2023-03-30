
while True:
    
    a=float(input("Digite um numero= "))
    b=float(input("Digite outro numero= "))
    operação=input("Digite a operação a realizar= ")
    if operação=='+':
        resultado=a+b
    elif operação=='-':
        resultado=a-b
    elif operação=='*':
        resultado=a*b
    elif operação=='/':
        resultado=a/b
    else:
        print("operação invalida! ")

        
        resultado=0
    print('Resultado ',resultado)

    
    