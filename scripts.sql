DROP DATABASE IF EXISTS academia;

create database academia;

create table alunos
(
    id       	int auto_increment,
    nome     	varchar(255) null,
    cpf      	varchar(255) null,
    idade    	varchar(255) null,
    mensalidade varchar(255) null,
    multa 	varchar(255) null,
    endereco 	varchar(255) null,
    telefone   	varchar(255) null,
    constraint pessoas_pk
        primary key (id)
);

create table professores
(
    id                int auto_increment,
    nome              varchar(255) null,
    cpf               varchar(255) null,
    salario           double       null,
    endereco          varchar(255) null,
    telefone          varchar(255) null,
    horas_trabalhadas varchar(255) null,
    constraint professores_pk
        primary key (id)
);

create table funcionarios
(
    id       int auto_increment,
    nome     varchar(255) null,
    salario  double       null,
    funcao   varchar(255) null,
    endereco varchar(255) null,
    telefone varchar(255) null,
    constraint funcionario_pk
        primary key (id)
);

create table convidados
(
    id    int auto_increment,
    nome  varchar(255) null,
    cpf   varchar(255) null,
    valor double       null,
    constraint convidados_pk
        primary key (id)
);





