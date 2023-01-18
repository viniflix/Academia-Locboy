import mysql.connector



class Conexao:
    def __init__(self,tabela):
        self.con = mysql.connector.connect(host='localhost', port='3306', database='teste_python', user='admin', password='12345')
        self.tabela = tabela

    def fechar(self, cursor):
        if self.con.is_connected():
            cursor.close()
            self.con.close()
            print('Conexão encerrada')

    def listar(self):
        if self.con.is_connected():
            command = 'SELECT * FROM ' + self.tabela
            cursor = self.con.cursor()
            cursor.execute(command)
            modelos = cursor.fetchall()
            self.fechar(cursor)

            return modelos


