-- Apaga as tabelas caso existam
DROP TABLE IF EXISTS Agendamento CASCADE;
DROP TABLE IF EXISTS Pagamento CASCADE;
DROP TABLE IF EXISTS Servicos CASCADE;
DROP TABLE IF EXISTS Seguradora CASCADE;
DROP TABLE IF EXISTS Clientes_particular CASCADE;
DROP TABLE IF EXISTS Funcionario CASCADE;

-- Tabela Clientes_particular
CREATE TABLE Clientes_particular (
    Cod_cliente INT PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20) ,
    email VARCHAR(255),
    CPF VARCHAR(11) NOT NULL UNIQUE,
    Endereço VARCHAR(255) 
);

-- Tabela Seguradora
CREATE TABLE Seguradora (
    Cod_cliente INT PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL UNIQUE,
    Nome VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20) ,
    email VARCHAR(255)
);


-- Tabela Funcionário
CREATE TABLE Funcionario (
    CPF VARCHAR(11) PRIMARY KEY,
    Especialidade VARCHAR(50),
    Nome VARCHAR(255) NOT NULL,
    Telefone VARCHAR(20),
    Cidade VARCHAR(100),
    Salario DOUBLE PRECISION CHECK (Salario > 0)
);

-- Tabela Serviços
CREATE TABLE Servicos (
    ID_serviço INT PRIMARY KEY,
    Especificações VARCHAR(255),
    Nome VARCHAR(255) NOT NULL,
    Cpf_func VARCHAR(11) NOT NULL,
    FOREIGN KEY (Cpf_func) REFERENCES Funcionario(CPF)
);
-- Tabela Agendamento
CREATE TABLE Agendamento (
    Cod_agendamento SERIAL PRIMARY KEY,
    Data DATE NOT NULL,
    Endereço VARCHAR(255) NOT NULL,
    Status VARCHAR(50),
    Descrição VARCHAR(255),
    Horário TIME ,
    Cod_Cliente INT NOT NULL,
    ID_serviço INT NOT NULL,
    FOREIGN KEY (Cod_Cliente) REFERENCES Clientes_particular(Cod_cliente),
    FOREIGN KEY (ID_serviço) REFERENCES Servicos(ID_serviço)
);

-- Tabela Pagamento
CREATE TABLE Pagamento (
    ID INT PRIMARY KEY,
    Data DATE NOT NULL,
    Valor DOUBLE PRECISION CHECK (Valor > 0),
    Forma_pg VARCHAR(50) ,
	ID_Agendamento int,
	FOREIGN KEY (ID_Agendamento) REFERENCES Agendamento(Cod_agendamento)
);
INSERT INTO Clientes_particular (Cod_cliente, Nome, Telefone, email, CPF, Endereço)
VALUES
    (1, 'João da Silva', '11-91234-5678', 'joao.silva@example.com', '12345678901', 'Rua A, 123, Santo André'),
    (2, 'Maria Oliveira', '11-99876-5432', 'maria.oliveira@example.com', '10987654321', 'Avenida B, 456, São Paulo'),
    (3, 'Carlos Santos', '11-93456-7890', 'carlos.santos@example.com', '23456789012', 'Rua C, 789, Mauá'),
    (4, 'Ana Paula', '11-91234-1234', 'ana.paula@example.com', '34567890123', 'Rua D, 1011, Itu'),
    (5, 'Pedro Costa', '11-92345-6789', 'pedro.costa@example.com', '45678901234', 'Avenida E, 1213, São Paulo'),
    (6, 'Laura Ferreira', '11-97654-3210', 'laura.ferreira@example.com', '56789012345', 'Rua F, 1415, Santo André');

-- Inserindo dados na tabela Seguradora
INSERT INTO Seguradora (Cod_cliente, CNPJ, Nome, Telefone, email)
VALUES
    (7, '12345678000199', 'Seguradora ABC', '11-91234-5678', 'contato@seguradoraabc.com'),
    (8, '98765432000188', 'Seguradora XYZ', '11-99876-5432', 'contato@seguradoraxyz.com');

-- Inserindo dados na tabela Funcionário
INSERT INTO Funcionario (CPF, Especialidade, Nome, Telefone, Cidade, Salario)
VALUES
    ('12345678901', 'Eletricista', 'José Eletricista', '11-91234-5678', 'São Paulo', 3000.00),
    ('10987654321', 'Dedetizador', 'Carlos Dedetizador', '11-99876-5432', 'Santo André', 2800.00),
    ('23456789012', 'Limpeza de Caixa de Água', 'Ana Limpeza', '11-93456-7890', 'Mauá', 2500.00);

-- Inserindo dados na tabela Serviços
INSERT INTO Servicos (ID_serviço, Especificações, Nome, Cpf_func)
VALUES
    (1, 'Instalação de fiação elétrica', 'Serviço de Eletricista', '12345678901'),
    (2, 'Dedetização completa', 'Serviço de Dedetização', '10987654321'),
    (3, 'Limpeza de caixa de água de 500L', 'Serviço de Limpeza de Caixa de Água', '23456789012');

-- Inserindo dados na tabela Agendamento
INSERT INTO Agendamento (Data, Endereço, Status, Descrição, Horário, Cod_Cliente, ID_serviço)
VALUES
    ('2024-09-27', 'Rua A, 123, Santo André', 'Pendente', 'Instalação de fiação elétrica', '09:00', 1, 1),
    ('2024-09-28', 'Avenida B, 456, São Paulo', 'Confirmado', 'Dedetização completa', '14:00', 2, 2),
    ('2024-09-29', 'Rua C, 789, Mauá', 'Concluído', 'Limpeza de caixa de água de 500L', '10:00', 3, 3);

-- Inserindo dados na tabela Pagamento
INSERT INTO Pagamento (ID, Data, Valor, Forma_pg, ID_Agendamento)
VALUES
    (1, '2024-09-27', 150.00, 'Cartão de Crédito', 1),
    (2, '2024-09-28', 200.00, 'Boleto', 2),
    (3, '2024-09-29', 100.00, 'Dinheiro', 3);
