class Pokemon:
    def __init__(self, nome, level, tipo, ataques):
        self.nome = nome
        self.level = level
        self.ataques = ataques
        self.tipo = tipo

    def ataque(self):
        print("O pokemon atacou")