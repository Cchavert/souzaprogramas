# E também podemos percorrer uma das listas, adicionando elementos à outra com o método append(), assim:
sacola = ['Laranja', 'Banana']

legumes = ['Xuxu', 'Batata']

for legume in legumes:
  
    sacola.append(legume)

print(sacola)