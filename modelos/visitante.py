from modelos.pessoa import Pessoa


class Visitante(Pessoa):
    def __init__(self, nome, cpf, valor):
        super().__init__(nome, cpf)
        self.valor = valor