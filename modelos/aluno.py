from modelos.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, mensalidade, multa, endereco, telefone):
        super().__init__(nome, cpf)
        self.idade = idade
        self.mensalidade = mensalidade
        self.multa = multa
        self.endereco = endereco
        self.telefone = telefone
