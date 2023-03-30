def jls_extract_def():
    nota1 = float (input("Digite sua primeira Nota: "))
    nota2 = float (input("Digite sua Segunda Nota: "))
    nota3 = float (input("Digite sua Segunda Nota: "))
    
    notafinal = (nota1+nota2+nota3)/3
    if notafinal <7:
         print("Aluno Reprovado",notafinal)
    else:
    
         print(" Aluno Aprovado: ")
    return notafinal


notafinal = jls_extract_def()

