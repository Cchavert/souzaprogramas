class Fila(object):
    def init(self):
        self.dados = []
 
    def insere(self, elemento):
        self.dados.append(elemento)
 
    def retira(self):
        return self.dados.pop(0)
 
    def vazia(self):
        return len(self.dados) == 0