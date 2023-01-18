from modelos.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, cpf, salario, endereco, telefone, horas_trabalhadas):
        super().__init__(nome, cpf)
        self.salario = salario
        self.endereco = endereco
        self.telefone = telefone
        self.horas_trabalhadas = horas_trabalhadas
