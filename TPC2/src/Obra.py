class Obra:
    def __init__(self, nome, descricao, anoCriacao, periodo, compositor, duracao, id):
        self.nome = nome
        self.descricao = descricao
        self.anoCriacao = anoCriacao
        self.periodo = periodo
        self.compositor = compositor
        self.duracao = duracao
        self.id = id

    def getNome(self):
        return self.nome

    def getDescricao(self):
        return self.descricao

    def getAnoCriacao(self):
        return self.anoCriacao

    def getPeriodo(self):
        return self.periodo

    def getCompositor(self):
        return self.compositor

    def getDuracao(self):
        return self.duracao

    def getId(self):
        return self.id