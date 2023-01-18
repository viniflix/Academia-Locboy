from modelos.pessoa import Pessoa


class Funcionario:
    def __init__(self, nome, salario, funcao, endereco, telefone):
        self.nome = nome
        self.salario = salario
        self.funcao = funcao
        self.endereco = endereco
        self.telefone = telefone
