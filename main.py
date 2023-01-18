from conexao.alunoBD import AlunoBD
from conexao.funcionarioBD import FuncionarioBD
from conexao.professorBD import ProfessorBD
from conexao.visitanteBD import VisitanteBD
from modelos.aluno import Aluno
from modelos.funcionario import Funcionario
from modelos.professor import Professor
from modelos.visitante import Visitante

while True:
    print('''bem-vindos                
    Escolha uma opção:
    [1]Cadastrar Novo Aluno
    [2]Cadastrar Novo Professor
    [3]Cadastro Novo Funcionario
    [4]Cadastro Novo Convidado
    [5]Listar alunos
    [6]Listar profissionais
    [7]Listar funcionários    
    [8]Listar convidados    
    [9]Sair ''')
    op = int(input())
    # Escolha da opcao
    if op == 1:
        nome = str(input('Insira o nome do cliente: '))
        cpf = str(input('Insira o cpf do cliente (xxx.xxx.xxx-xx): '))
        idade = int(input('Insira a idade do cliente: '))
        while idade < 10:
            print('Idade nao pode ser inferior 10')
            idade = int(input('Insira a idade do cliente: '))
        print('''Escolha o plano:
            [1]Basico   - R$ 70.00
            [2]Medio    - R$ 90.00
            [3]Completo - R$ 120.00''')
        plano = int(input())
        mensalidade = '0'
        while plano != 1 and plano != 2 and plano != 3:
            print('Escolha um plano valido')
            plano = int(input())
            if plano == 1:
                mensalidade = '70'
            if plano == 2:
                mensalidade = '90'
            if plano == 3:
                mensalidade = '120'
        multa = str(input('Insira a multa por atraso do cliente: '))
        endereco = str(input('Insira o endereço do cliente: '))
        telefone = str(input('Insira o telefone do cliente ((xx)xxxxx-xxxx): '))
        aluno = Aluno(nome, cpf, idade, mensalidade, multa, endereco, telefone)
        alunoBD = AlunoBD()
        alunoBD.inserir(aluno)

    elif op == 2:

        nome = str(input("Digite o nome: "))
        cpf = str(input("Digite o cpf: "))
        salario = float(input("Digite o salario: "))
        while salario <= 0:
            salario = float(input("Informe um salario superio a 0: "))
        endereco = str(input("Digite o endereço: "))
        telefone = str(input("Digite o telefone: "))
        horas_trabalhadas = str(input("Digite sas horas trabalhadas: "))

        professor = Professor(nome, cpf, salario, endereco, telefone, horas_trabalhadas)
        professorBD = ProfessorBD()
        professorBD.inserir(professor)


    elif op == 3:
        nome = str(input("Nome: "))
        salario = float(input("Salario: "))
        while salario <= 0:
            salario = float(input("Informe um salario superior a 0: "))
        funcao = str(input("Funçao: "))
        endereco = str(input("Endereço: "))
        telefone = str(input("Telefone: "))
        funcionario = Funcionario(nome, salario, funcao, endereco, telefone)
        funcionarioBD = FuncionarioBD()
        funcionarioBD.inserir(funcionario)

    elif op == 4:
        nome = str(input("Nome: "))
        cpf = str(input("CPF: "))
        valor = float(input("Valor a ser pago: "))
        while valor <= 0:
            valor = float(input("Informe um salario superior a 0: "))
        visitante = Visitante(nome, cpf, valor)
        visitanteBD = VisitanteBD()
        visitanteBD.inserir(visitante)

    elif op == 5:
        print("Listar alunos")
        alunoBD = AlunoBD()
        print(alunoBD.listar())

    elif op == 6:
        print("Listar profissionais")
        professorBD = ProfessorBD()
        print(professorBD.listar())

    elif op == 7:
        print("Listar funcionários")
        funcionarioBD = FuncionarioBD()
        print(funcionarioBD.listar())

    elif op == 8:
        print("Listar Convidados")
        visitanteBD = VisitanteBD()
        print(visitanteBD.listar())

    elif op == 9:
        print("saindo...")
        exit()

