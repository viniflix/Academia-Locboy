from conexao.conexao import Conexao


class VisitanteBD(Conexao):
    def __init__(self):
        super().__init__("convidados")

    def inserir(self, visitante):
        if self.con.is_connected():
            command = 'SELECT * FROM ' + self.tabela + ' WHERE cpf = \'' + visitante.cpf + '\''
            cursor = self.con.cursor()
            cursor.execute(command)
            modelos = cursor.fetchall()

            if modelos:
                print('O cpf informado ja se econtra cadastrado\nPor favor informe outro cpf')
                self.fechar(cursor)
                return

            dados = '\'' + visitante.nome + '\',\'' + visitante.cpf + '\'' + ',' + str(visitante.valor) + ')'
            command = """INSERT INTO convidados (nome, cpf, valor) VALUES ("""
            sql = command + dados
            print(sql)
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            self.fechar(cursor)
