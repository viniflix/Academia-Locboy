from conexao.conexao import Conexao


class AlunoBD(Conexao):

    def __init__(self):
        super().__init__('alunos')

    def inserir(self, aluno):
        if self.con.is_connected():
            command = 'SELECT * FROM ' + self.tabela + ' WHERE cpf = \'' + aluno.cpf + '\''
            cursor = self.con.cursor()
            cursor.execute(command)
            modelos = cursor.fetchall()
            if modelos:
                print('O cpf informado ja se econtra cadastrado\nPor favor informe outro cpf')
                self.fechar(cursor)
                return

            dados = '\'' + aluno.nome + '\',\'' + aluno.cpf + '\'' + ',' + str(aluno.idade) + ',\'' + aluno.mensalidade + '\',\'' + aluno.multa + '\',\'' + aluno.endereco + '\',\'' + aluno.telefone + '\')'
            command = """INSERT INTO alunos (nome, cpf, idade, mensalidade, multa, endereco, telefone) VALUES ("""
            sql = command + dados
            cursor.execute(sql)
            self.con.commit()
            self.fechar(cursor)

