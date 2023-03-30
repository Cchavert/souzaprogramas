acougue=[]

senha=input("Senha de usuario :")
usuario=input("Usuario :")
for i in range(2):
    while usuario==senha:
        print("Senha deve ser diferente de usuario:")
        senha=input("senha: ")
        print("Loguin ok: ")