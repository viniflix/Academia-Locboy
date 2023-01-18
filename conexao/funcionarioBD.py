from conexao.conexao import Conexao


class FuncionarioBD(Conexao):
    def __init__(self):
        super().__init__('funcionarios')

    def inserir(self, funcionario):
        if self.con.is_connected():
            dados = '\'' + funcionario.nome + '\',' + str(funcionario.salario) + ',\'' + funcionario.funcao + '\',\'' + funcionario.endereco + '\',\'' + funcionario.telefone + '\')'
            command = """INSERT INTO funcionarios (nome, salario, funcao, endereco, telefone) VALUES ("""
            sql = command + dados
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            self.fechar(cursor)