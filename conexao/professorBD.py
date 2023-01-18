from conexao.conexao import Conexao


class ProfessorBD(Conexao):
    def __init__(self):
        super().__init__("professores")

    def inserir(self, professor):
        if self.con.is_connected():
            command = 'SELECT * FROM ' + self.tabela + ' WHERE cpf = \'' + professor.cpf + '\''
            cursor = self.con.cursor()
            cursor.execute(command)
            modelos = cursor.fetchall()
            if modelos:
                print('O cpf informado ja se econtra cadastrado\nPor favor informe outro cpf')
                self.fechar(cursor)
                return

            dados = '\'' + professor.nome + '\',\'' + professor.cpf + '\'' + ',' + str(professor.salario) + ',\'' + professor.endereco + '\',\'' + professor.telefone + '\',\'' + professor.horas_trabalhadas +'\')'
            command = """INSERT INTO professores (nome, cpf, salario, endereco, telefone, horas_trabalhadas) VALUES ("""
            sql = command + dados
            print(sql)
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            self.fechar(cursor)
