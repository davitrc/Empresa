from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font
import psycopg2

#$$$$$$$$$$$$$$$$$ Conectando ao Banco $$$$$$$$$$$$$$$$
def connect_db():   
    try:
        conn = psycopg2.connect(
            dbname='Empresa_Faz_Tudo',
            user='postgres',
            password='root',
            host='localhost',
            port='5432'
        )
        return conn
    except Exception as e:
        messagebox.showerror("Erro", f"Erro na conexão: {e}")

#=================Cadastro pagamento=================
def cadastro_pagamento():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    global DataEntry, ValorEntry, Forma_pgEntry, ID_pgEntry,ID_AgenEntry

    DataLabel = Label(RightFrame, text="Data (Ano-mês-dia): ", font=("Arial", 20), bg="#FFE5B4")
    DataLabel.place(x=20, y=10)
    DataEntry = Entry(RightFrame, width=40)
    DataEntry.place(x=300, y=20)

    ValorLabel = Label(RightFrame, text="Valor: ", font=("Arial", 20), bg="#FFE5B4")
    ValorLabel.place(x=20, y=50)
    ValorEntry = Entry(RightFrame, width=40)
    ValorEntry.place(x=300, y=60)

    Forma_pgLabel = Label(RightFrame, text="Forma de Pagamento: ", font=("Arial", 20), bg="#FFE5B4")
    Forma_pgLabel.place(x=20, y=100)
    Forma_pgEntry = Entry(RightFrame, width=40)
    Forma_pgEntry.place(x=300, y=110)

    ID_pgLabel = Label(RightFrame, text="ID do Pagamento: ", font=("Arial", 20), bg="#FFE5B4")
    ID_pgLabel.place(x=20, y=150)
    ID_pgEntry = Entry(RightFrame, width=40)
    ID_pgEntry.place(x=300, y=160)

    ID_AgenLabel = Label(RightFrame, text="ID do Agendamento: ", font=("Arial", 20), bg="#FFE5B4")
    ID_AgenLabel.place(x=20, y=200)
    ID_AgenEntry = Entry(RightFrame, width=40)
    ID_AgenEntry.place(x=300, y=210)

    # Botão para cadastrar cliente
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar",width=40,command=cadastrar_pagamento)
    btn_cadastrar.place(x=220, y=300)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

def cadastrar_pagamento():
    # Coleta os dados dos campos de entrada
    data = DataEntry.get()
    valor = ValorEntry.get()
    forma_pg = Forma_pgEntry.get()
    id_pg = ID_pgEntry.get()
    id_ag = ID_AgenEntry.get()

    # Validação básica dos dados
    if not (data and valor and forma_pg and id_pg and id_ag):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return


    # Conexão com o banco de dados
    conn = connect_db()
    cursor = conn.cursor()

    
    try:
        # Insere os dados na tabela Pagamento
        insert_query = """
        INSERT INTO Pagamento (ID, Data, Valor, Forma_pg,ID_Agendamento)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (id_pg, data, valor, forma_pg,id_ag))

        # Salva as alterações
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Pagamento cadastrado com sucesso!")

    except Exception as e:
        # Mensagem de erro
        messagebox.showerror("Erro", f"Erro ao cadastrar pagamento: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão
#=================Cadastro serviço===================
def cadastro_servico():
    for widget in RightFrame.winfo_children():
        widget.place_forget()
    global Nome_ServicoEntry, EspecificacoesEntry, Cpf_FuncEntry, ID_ServicoEntry

    Nome_ServicoLabel = Label(RightFrame, text="Nome do Serviço: ", font=("Arial", 20), bg="#FFE5B4")
    Nome_ServicoLabel.place(x=20, y=10)
    Nome_ServicoEntry = Entry(RightFrame, width=40)
    Nome_ServicoEntry.place(x=300, y=20)

    EspecificacoesLabel = Label(RightFrame, text="Especificações: ", font=("Arial", 20), bg="#FFE5B4")
    EspecificacoesLabel.place(x=20, y=50)
    EspecificacoesEntry = Entry(RightFrame, width=40)
    EspecificacoesEntry.place(x=300, y=60)

    Cpf_FuncLabel = Label(RightFrame, text="CPF do Funcionário: ", font=("Arial", 20), bg="#FFE5B4")
    Cpf_FuncLabel.place(x=20, y=100)
    Cpf_FuncEntry = Entry(RightFrame, width=40)
    Cpf_FuncEntry.place(x=300, y=110)

    ID_ServicoLabel = Label(RightFrame, text="ID do Serviço: ", font=("Arial", 20), bg="#FFE5B4")
    ID_ServicoLabel.place(x=20, y=150)
    ID_ServicoEntry = Entry(RightFrame, width=40)
    ID_ServicoEntry.place(x=300, y=160)

    # Botão para cadastrar cliente
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar",width=40,command=cadastrar_servico)
    btn_cadastrar.place(x=220, y=300)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

def cadastrar_servico():
    # Coleta os dados dos campos de entrada
    nome_servico = Nome_ServicoEntry.get()
    especificacoes = EspecificacoesEntry.get()
    cpf_func = Cpf_FuncEntry.get()
    id_servico = ID_ServicoEntry.get()

    # Validação básica dos dados
    if not (nome_servico and especificacoes and cpf_func and id_servico):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    

    # Conexão com o banco de dados
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Insere os dados na tabela Servicos
        insert_query = """
        INSERT INTO Servicos (ID_serviço, Especificações, Nome, Cpf_func)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (id_servico, especificacoes, nome_servico, cpf_func))

        # Salva as alterações
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Serviço cadastrado com sucesso!")

    except Exception as e:
        # Mensagem de erro
        messagebox.showerror("Erro", f"Erro ao cadastrar serviço: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão
#=================Cadastro Agendamento=================
def cadastro_agendamento():
    for widget in RightFrame.winfo_children():
        widget.place_forget()
    
    global DataEntry, EnderecoEntry, StatusEntry, DescricaoEntry, HorarioEntry, CodClienteEntry, IDServicoEntry

    DataLabel = Label(RightFrame, text="Data (Ano-Mês-Dia): ", font=("Arial", 20), bg="#FFE5B4")
    DataLabel.place(x=20, y=10)
    DataEntry = Entry(RightFrame, width=40)
    DataEntry.place(x=300, y=20)

    EnderecoLabel = Label(RightFrame, text="Endereço: ", font=("Arial", 20), bg="#FFE5B4")
    EnderecoLabel.place(x=20, y=50)
    EnderecoEntry = Entry(RightFrame, width=40)
    EnderecoEntry.place(x=300, y=60)

    StatusLabel = Label(RightFrame, text="Status: ", font=("Arial", 20), bg="#FFE5B4")
    StatusLabel.place(x=20, y=100)
    StatusEntry = Entry(RightFrame, width=40)
    StatusEntry.place(x=300, y=110)

    DescricaoLabel = Label(RightFrame, text="Descrição: ", font=("Arial", 20), bg="#FFE5B4")
    DescricaoLabel.place(x=20, y=150)
    DescricaoEntry = Entry(RightFrame, width=40)
    DescricaoEntry.place(x=300, y=160)

    HorarioLabel = Label(RightFrame, text="Horário (HH:MM): ", font=("Arial", 20), bg="#FFE5B4")
    HorarioLabel.place(x=20, y=200)
    HorarioEntry = Entry(RightFrame, width=40)
    HorarioEntry.place(x=300, y=210)

    CodClienteLabel = Label(RightFrame, text="Código do Cliente: ", font=("Arial", 20), bg="#FFE5B4")
    CodClienteLabel.place(x=20, y=250)
    CodClienteEntry = Entry(RightFrame, width=40)
    CodClienteEntry.place(x=300, y=260)

    IDServicoLabel = Label(RightFrame, text="ID do Serviço: ", font=("Arial", 20), bg="#FFE5B4")
    IDServicoLabel.place(x=20, y=300)
    IDServicoEntry = Entry(RightFrame, width=40)
    IDServicoEntry.place(x=300, y=310)

    # Botão para cadastrar cliente
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar", width=40, command=cadastrar_agendamento)
    btn_cadastrar.place(x=220, y=450)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

def cadastrar_agendamento():
    # Coleta os dados dos campos de entrada
    data = DataEntry.get()
    endereco = EnderecoEntry.get()
    status = StatusEntry.get()
    descricao = DescricaoEntry.get()
    horario = HorarioEntry.get()
    cod_cliente = CodClienteEntry.get()
    id_servico = IDServicoEntry.get()

    # Validação básica dos dados
    if not all([data, endereco, status, descricao, horario, cod_cliente, id_servico]):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return


    # Conexão com o banco de dados
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Insere os dados na tabela Agendamento
        insert_query = """
        INSERT INTO Agendamento (Data, Endereço, Status, Descrição, Horário, Cod_Cliente, ID_serviço)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (data, endereco, status, descricao, horario, cod_cliente, id_servico))

        # Salva as alterações
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Agendamento cadastrado com sucesso!")

    except Exception as e:
        # Mensagem de erro
        messagebox.showerror("Erro", f"Erro ao cadastrar agendamento: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão
#=================Cadastro Seguradora==================
def cadastro_seguradora():
    for widget in RightFrame.winfo_children():
        widget.place_forget()
    
    global Nome_SeguradoraEntry, Telefone_SeguradoraEntry, Email_SeguradoraEntry, CNPJ_SeguradoraEntry, Cod_SeguradoraEntry


    Nome_SeguradoraLabel = Label(RightFrame, text="Nome da Seguradora: ", font=("Arial", 20), bg="#FFE5B4")
    Nome_SeguradoraLabel.place(x=20, y=10)
    Nome_SeguradoraEntry = Entry(RightFrame, width=40)
    Nome_SeguradoraEntry.place(x=300, y=20)

    Telefone_SeguradoraLabel = Label(RightFrame, text="Telefone: ", font=("Arial", 20), bg="#FFE5B4")
    Telefone_SeguradoraLabel.place(x=20, y=50)
    Telefone_SeguradoraEntry = Entry(RightFrame, width=40)
    Telefone_SeguradoraEntry.place(x=300, y=60)

    Email_SeguradoraLabel = Label(RightFrame, text="Email: ", font=("Arial", 20), bg="#FFE5B4")
    Email_SeguradoraLabel.place(x=20, y=100)
    Email_SeguradoraEntry = Entry(RightFrame, width=40)
    Email_SeguradoraEntry.place(x=300, y=110)

    CNPJ_SeguradoraLabel = Label(RightFrame, text="CNPJ: ", font=("Arial", 20), bg="#FFE5B4")
    CNPJ_SeguradoraLabel.place(x=20, y=150)
    CNPJ_SeguradoraEntry = Entry(RightFrame, width=40)
    CNPJ_SeguradoraEntry.place(x=300, y=160)

    Cod_SeguradoraLabel = Label(RightFrame, text="Código Seguradora: ", font=("Arial", 20), bg="#FFE5B4")
    Cod_SeguradoraLabel.place(x=20, y=200)
    Cod_SeguradoraEntry = Entry(RightFrame, width=40)
    Cod_SeguradoraEntry.place(x=300, y=210)

    # Botão para cadastrar cliente
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar",width=40,command=cadastrar_seguradora)
    btn_cadastrar.place(x=220, y=300)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

def cadastrar_seguradora():
    # Coleta os dados dos campos de entrada
    nome = Nome_SeguradoraEntry.get()
    telefone = Telefone_SeguradoraEntry.get()
    email = Email_SeguradoraEntry.get()
    cnpj = CNPJ_SeguradoraEntry.get()
    cod_seguradora = Cod_SeguradoraEntry.get()

    # Validação básica dos dados
    if not all([nome, telefone, email, cnpj, cod_seguradora]):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    # Conexão com o banco de dados
    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Insere os dados na tabela Seguradora
        insert_query = """
        INSERT INTO Seguradora (Cod_cliente, CNPJ, Nome, Telefone, email)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (cod_seguradora, cnpj, nome, telefone, email))

        # Salva as alterações
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Seguradora cadastrada com sucesso!")

    except Exception as e:
        # Mensagem de erro
        messagebox.showerror("Erro", f"Erro ao cadastrar seguradora: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão
#=================Cadastro Funcionarios=================
def cadastro_funcionario():
    for widget in RightFrame.winfo_children():
        widget.place_forget()
    
    global Nome_FuncEntry, Telefone_FuncEntry, Cidade_FuncEntry, EspecialidadeEntry, Cpf_FuncEntry, SalarioEntry

    Nome_FuncLabel = Label(RightFrame, text="Nome: ", font=("Arial", 20), bg="#FFE5B4")
    Nome_FuncLabel.place(x=20, y=10)
    Nome_FuncEntry = Entry(RightFrame, width=40)
    Nome_FuncEntry.place(x=250, y=20)

    Telefone_FuncLabel = Label(RightFrame, text="Telefone: ", font=("Arial", 20), bg="#FFE5B4")
    Telefone_FuncLabel.place(x=20, y=50)
    Telefone_FuncEntry = Entry(RightFrame, width=40)
    Telefone_FuncEntry.place(x=250, y=60)

    Cidade_FuncLabel = Label(RightFrame, text="Cidade: ", font=("Arial", 20), bg="#FFE5B4")
    Cidade_FuncLabel.place(x=20, y=100)
    Cidade_FuncEntry = Entry(RightFrame, width=40)
    Cidade_FuncEntry.place(x=250, y=110)

    EspecialidadeLabel = Label(RightFrame, text="Especialidade: ", font=("Arial", 20), bg="#FFE5B4")
    EspecialidadeLabel.place(x=20, y=150)
    EspecialidadeEntry = Entry(RightFrame, width=40)
    EspecialidadeEntry.place(x=250, y=160)

    Cpf_FuncLabel = Label(RightFrame, text="CPF: ", font=("Arial", 20), bg="#FFE5B4")
    Cpf_FuncLabel.place(x=20, y=200)
    Cpf_FuncEntry = Entry(RightFrame, width=40)
    Cpf_FuncEntry.place(x=250, y=210)

    SalarioLabel = Label(RightFrame, text="Salário: ", font=("Arial", 20), bg="#FFE5B4")
    SalarioLabel.place(x=20, y=250)
    SalarioEntry = Entry(RightFrame, width=40)
    SalarioEntry.place(x=250, y=260)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

    # Botão para cadastrar funcionario
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar", width=40, command=cadastrar_funcionario)
    btn_cadastrar.place(x=220, y=300)

def cadastrar_funcionario():
    nome_func = Nome_FuncEntry.get()
    telefone = Telefone_FuncEntry.get()
    cidade = Cidade_FuncEntry.get()
    especialidade = EspecialidadeEntry.get()
    cpf_func = Cpf_FuncEntry.get()
    salario = SalarioEntry.get()

    # Validação básica dos dados
    if not (nome_func and telefone and cidade and especialidade and cpf_func and salario):
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    conn = connect_db()
    cursor = conn.cursor()

    try:
        insert_query = """
        INSERT INTO Funcionario (CPF, Nome, Telefone, Cidade, Especialidade, Salario)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (cpf_func, nome_func, telefone, cidade, especialidade, salario))
        conn.commit()
        messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar funcionário: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão
#=================Cadastro Cliente===============
def cadastro_cliente():
    for widget in RightFrame.winfo_children():
        widget.place_forget()
    
    global Nome_ClienteEntry, Tel_ClienteEntry, Email_ClienteEntry, CPF_ClienteEntry, Endereco_ClienteEntry, Cod_ClienteEntry

    Nome_ClienteLabel = Label(RightFrame, text="Nome: ", font=("Arial", 20), bg="#FFE5B4")
    Nome_ClienteLabel.place(x=20, y=10)
    Nome_ClienteEntry = Entry(RightFrame, width=40)
    Nome_ClienteEntry.place(x=250, y=20)

    Tel_ClienteLabel = Label(RightFrame, text="Telefone: ", font=("Arial", 20), bg="#FFE5B4")
    Tel_ClienteLabel.place(x=20, y=50)
    Tel_ClienteEntry = Entry(RightFrame, width=40)
    Tel_ClienteEntry.place(x=250, y=60)

    Email_ClienteLabel = Label(RightFrame, text="Email: ", font=("Arial", 20), bg="#FFE5B4")
    Email_ClienteLabel.place(x=20, y=100)
    Email_ClienteEntry = Entry(RightFrame, width=40)
    Email_ClienteEntry.place(x=250, y=110)

    CPF_ClienteLabel = Label(RightFrame, text="CPF: ", font=("Arial", 20), bg="#FFE5B4")
    CPF_ClienteLabel.place(x=20, y=150)
    CPF_ClienteEntry = Entry(RightFrame, width=40)
    CPF_ClienteEntry.place(x=250, y=160)

    Endereco_ClienteLabel = Label(RightFrame, text="Endereço: ", font=("Arial", 20), bg="#FFE5B4")
    Endereco_ClienteLabel.place(x=20, y=200)
    Endereco_ClienteEntry = Entry(RightFrame, width=40)
    Endereco_ClienteEntry.place(x=250, y=210)

    Cod_ClienteLabel = Label(RightFrame, text="Código Cliente: ", font=("Arial", 20), bg="#FFE5B4")
    Cod_ClienteLabel.place(x=20, y=250)
    Cod_ClienteEntry = Entry(RightFrame, width=40)
    Cod_ClienteEntry.place(x=250, y=260)

    # Botão para cadastrar cliente
    btn_cadastrar = ttk.Button(RightFrame, text="Cadastrar",width=40,command=cadastrar_cliente)
    btn_cadastrar.place(x=220, y=300)

    # Botão Voltar_Cadastro
    Voltar_pgCadastro = ttk.Button(RightFrame, text="Voltar", width=64, command=cadastrar)
    Voltar_pgCadastro.place(x=130, y=550)

def cadastrar_cliente():
    # Coleta os dados dos campos de entrada
    nome = Nome_ClienteEntry.get()
    telefone = Tel_ClienteEntry.get()
    email = Email_ClienteEntry.get()
    cpf = CPF_ClienteEntry.get()
    endereco = Endereco_ClienteEntry.get()
    cod_cliente = Cod_ClienteEntry.get()

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Insere os dados na tabela Clientes_particular
        insert_query = """
        INSERT INTO Clientes_particular (Cod_cliente, Nome, Telefone, email, CPF, Endereço)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (cod_cliente, nome, telefone, email, cpf, endereco))

        # Salva as alterações
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

    except Exception as e:
        # Mensagem de erro
        messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {e}")

    finally:
        cursor.close()  # Fechar o cursor
        conn.close()    # Fechar a conexão

#=========Configurando botao cadastro============

def cadastrar():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Cad_Label= Label(RightFrame,text="O que você deseja cadastrar: ",font=("Arial", 20),bg="#FFE5B4")
    Cad_Label.place(x=20,y=10)

    CadCliente = ttk.Button(RightFrame, text="Novo Cliente", width=32,style="Custom.TButton",command=cadastro_cliente)
    CadCliente.place(x=130, y=60)

    CadSeguradora = ttk.Button(RightFrame, text="Nova Seguradora", width=32,style="Custom.TButton",command=cadastro_seguradora)
    CadSeguradora.place(x=130, y=140)

    CadFuncionario = ttk.Button(RightFrame, text="Novo Funcionário", width=32,style="Custom.TButton",command=cadastro_funcionario)
    CadFuncionario.place(x=130, y=220)

    CadServico = ttk.Button(RightFrame, text="Novo Serviço", width=32,style="Custom.TButton",command=cadastro_servico)
    CadServico.place(x=130, y=300)

    CadPagamento = ttk.Button(RightFrame, text="Pagamento", width=32,style="Custom.TButton",command=cadastro_pagamento)
    CadPagamento.place(x=130, y=380)

    CadAgendamento = ttk.Button(RightFrame, text="Angendamento", width=32,style="Custom.TButton",command=cadastro_agendamento)
    CadAgendamento.place(x=130, y=460)

    # Botão Voltar_Registro
    Voltar_pgRegistro = ttk.Button(RightFrame, text="Voltar", width=64, command=voltar_Registro)
    Voltar_pgRegistro.place(x=130, y=550)


def voltar_Registro():

    for widget in RightFrame.winfo_children():
        widget.place_forget()

    # Mostra os botões originais
    CadastroButton.place(x=130, y=200)
    ConsultaButton.place(x=130, y=300)


#============Consulta Cliente===================
def consultar_clientes():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Clientes: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos", command=lambda: consultar_clientes_db())
    todos_button.place(x=20, y=50)

    nome_label = Label(RightFrame, text="Nome: ", font=("Arial", 14), bg="#FFE5B4")
    nome_label.place(x=20, y=100)
    nome_entry = Entry(RightFrame, width=30)
    nome_entry.place(x=200, y=105)
    nome_button = ttk.Button(RightFrame, text="Consultar por Nome", command=lambda: consultar_clientes_db(nome=nome_entry.get()))
    nome_button.place(x=350, y=102)

    cod_cliente_label = Label(RightFrame, text="Código cliente: ", font=("Arial", 14), bg="#FFE5B4")
    cod_cliente_label.place(x=20, y=150)
    cod_cliente_entry = Entry(RightFrame, width=30)
    cod_cliente_entry.place(x=200, y=155)
    cod_cliente_button = ttk.Button(RightFrame, text="Consultar por Código", command=lambda: consultar_clientes_db(cod_cliente=cod_cliente_entry.get()))
    cod_cliente_button.place(x=350, y=152)

    cpf_label = Label(RightFrame, text="CPF: ", font=("Arial", 14), bg="#FFE5B4")
    cpf_label.place(x=20, y=200)
    cpf_entry = Entry(RightFrame, width=30)
    cpf_entry.place(x=200, y=205)
    cpf_button = ttk.Button(RightFrame, text="Consultar por CPF", command=lambda: consultar_clientes_db(cpf=cpf_entry.get()))
    cpf_button.place(x=350, y=202)

    telefone_label = Label(RightFrame, text="Telefone: ", font=("Arial", 14), bg="#FFE5B4")
    telefone_label.place(x=20, y=250)
    telefone_entry = Entry(RightFrame, width=30)
    telefone_entry.place(x=200, y=255)
    telefone_button = ttk.Button(RightFrame, text="Consultar por Telefone", command=lambda: consultar_clientes_db(telefone=telefone_entry.get()))
    telefone_button.place(x=350, y=252)

    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)

def consultar_clientes_db(nome=None, cod_cliente=None, cpf=None, telefone=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Clientes_particular WHERE 1=1"
    params = []

    if nome:
        query += " AND Nome LIKE %s"
        params.append(f"%{nome}%")

    if cod_cliente:
        query += " AND Cod_cliente = %s"
        params.append(cod_cliente)

    if cpf:
        query += " AND CPF = %s"
        params.append(cpf)

    if telefone:
        query += " AND Telefone = %s"
        params.append(telefone)

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            # Aqui você pode exibir os resultados em uma nova janela ou em uma tabela
            messagebox.showinfo("Resultados", f"Clientes encontrados: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhum cliente encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar clientes: {e}")

    finally:
        cursor.close()
        conn.close()

#============Consulta Seguradoras===================
def consultar_seguradora():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Seguradoras: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos", command=lambda: consultar_seguradora_db())
    todos_button.place(x=20, y=50)

    nome_label = Label(RightFrame, text="Nome: ", font=("Arial", 14), bg="#FFE5B4")
    nome_label.place(x=20, y=100)
    nome_entry = Entry(RightFrame, width=30)
    nome_entry.place(x=200, y=105)
    nome_button = ttk.Button(RightFrame, text="Consultar por Nome", command=lambda: consultar_seguradora_db(nome=nome_entry.get()))
    nome_button.place(x=350, y=102)

    cod_cliente_label = Label(RightFrame, text="Código cliente: ", font=("Arial", 14), bg="#FFE5B4")
    cod_cliente_label.place(x=20, y=150)
    cod_cliente_entry = Entry(RightFrame, width=30)
    cod_cliente_entry.place(x=200, y=155)
    cod_cliente_button = ttk.Button(RightFrame, text="Consultar por Código", command=lambda: consultar_seguradora_db(cod_cliente=cod_cliente_entry.get()))
    cod_cliente_button.place(x=350, y=152)

    cnpj_label = Label(RightFrame, text="CNPJ: ", font=("Arial", 14), bg="#FFE5B4")
    cnpj_label.place(x=20, y=200)
    cnpj_entry = Entry(RightFrame, width=30)
    cnpj_entry.place(x=200, y=205)
    cnpj_button = ttk.Button(RightFrame, text="Consultar por CNPJ", command=lambda: consultar_seguradora_db(cnpj=cnpj_entry.get()))
    cnpj_button.place(x=350, y=202)

    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)

def consultar_seguradora_db(nome=None, cod_cliente=None, cnpj=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Seguradora WHERE 1=1"
    params = []

    if nome:
        query += " AND Nome LIKE %s"
        params.append(f"%{nome}%")

    if cod_cliente:
        query += " AND Cod_cliente = %s"
        params.append(cod_cliente)

    if cnpj:
        query += " AND CNPJ = %s"
        params.append(cnpj)

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            # Aqui você pode exibir os resultados em uma nova janela ou em uma tabela
            messagebox.showinfo("Resultados", f"Seguradoras encontradas: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhuma seguradora encontrada.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar seguradoras: {e}")

    finally:
        cursor.close()
        conn.close()

#============Consulta Funcionarios===================
def consultar_funcionarios():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Funcionários: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos", command=lambda: consultar_funcionarios_db())
    todos_button.place(x=20, y=50)

    nome_label = Label(RightFrame, text="Nome: ", font=("Arial", 14), bg="#FFE5B4")
    nome_label.place(x=20, y=100)
    nome_entry = Entry(RightFrame, width=30)
    nome_entry.place(x=250, y=105)
    nome_button = ttk.Button(RightFrame, text="Consultar por Nome", command=lambda: consultar_funcionarios_db(nome=nome_entry.get()))
    nome_button.place(x=350, y=102)

    cpf_label = Label(RightFrame, text="CPF: ", font=("Arial", 14), bg="#FFE5B4")
    cpf_label.place(x=20, y=150)
    cpf_entry = Entry(RightFrame, width=30)
    cpf_entry.place(x=250, y=155)
    cpf_button = ttk.Button(RightFrame, text="Consultar por CPF", command=lambda: consultar_funcionarios_db(cpf=cpf_entry.get()))
    cpf_button.place(x=350, y=152)

    especialidade_label = Label(RightFrame, text="Especialidade: ", font=("Arial", 14), bg="#FFE5B4")
    especialidade_label.place(x=20, y=200)
    especialidade_entry = Entry(RightFrame, width=30)
    especialidade_entry.place(x=250, y=205)
    especialidade_button = ttk.Button(RightFrame, text="Consultar por Especialidade", command=lambda: consultar_funcionarios_db(especialidade=especialidade_entry.get()))
    especialidade_button.place(x=350, y=202)

    cidade_label = Label(RightFrame, text="Cidade: ", font=("Arial", 14), bg="#FFE5B4")
    cidade_label.place(x=20, y=250)
    cidade_entry = Entry(RightFrame, width=30)
    cidade_entry.place(x=250, y=255)
    cidade_button = ttk.Button(RightFrame, text="Consultar por Cidade", command=lambda: consultar_funcionarios_db(cidade=cidade_entry.get()))
    cidade_button.place(x=350, y=252)

    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)
    
def consultar_funcionarios_db(nome=None, cpf=None, especialidade=None, cidade=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Funcionario WHERE 1=1"
    params = []

    if nome:
        query += " AND Nome LIKE %s"
        params.append(f"%{nome}%")

    if cpf:
        query += " AND CPF = %s"
        params.append(cpf)

    if especialidade:
        query += " AND Especialidade LIKE %s"
        params.append(f"%{especialidade}%")

    if cidade:
        query += " AND Cidade LIKE %s"
        params.append(f"%{cidade}%")

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            # Aqui você pode exibir os resultados em uma nova janela ou em uma tabela
            messagebox.showinfo("Resultados", f"Funcionários encontrados: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhum funcionário encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar funcionários: {e}")

    finally:
        cursor.close()
        conn.close()

#============Consulta Serviços===================
def consultar_servicos():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Serviços: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos", command=lambda: consultar_servicos_db())
    todos_button.place(x=20, y=50)

    nome_label = Label(RightFrame, text="Nome: ", font=("Arial", 14), bg="#FFE5B4")
    nome_label.place(x=20, y=100)
    nome_entry = Entry(RightFrame, width=30)
    nome_entry.place(x=250, y=105)
    nome_button = ttk.Button(RightFrame, text="Consultar por Nome", command=lambda: consultar_servicos_db(nome=nome_entry.get()))
    nome_button.place(x=350, y=102)

    especificacoes_label = Label(RightFrame, text="Especificações: ", font=("Arial", 14), bg="#FFE5B4")
    especificacoes_label.place(x=20, y=150)
    especificacoes_entry = Entry(RightFrame, width=30)
    especificacoes_entry.place(x=250, y=155)
    especificacoes_button = ttk.Button(RightFrame, text="Consultar por Especificações", command=lambda: consultar_servicos_db(especificacoes=especificacoes_entry.get()))
    especificacoes_button.place(x=350, y=152)

    id_label = Label(RightFrame, text="ID: ", font=("Arial", 14), bg="#FFE5B4")
    id_label.place(x=20, y=200)
    id_entry = Entry(RightFrame, width=30)
    id_entry.place(x=250, y=205)
    id_button = ttk.Button(RightFrame, text="Consultar por ID", command=lambda: consultar_servicos_db(id=id_entry.get()))
    id_button.place(x=350, y=202)

    cpf_funcionario_label = Label(RightFrame, text="CPF do Funcionário: ", font=("Arial", 14), bg="#FFE5B4")
    cpf_funcionario_label.place(x=20, y=250)
    cpf_funcionario_entry = Entry(RightFrame, width=30)
    cpf_funcionario_entry.place(x=250, y=255)
    cpf_funcionario_button = ttk.Button(RightFrame, text="Consultar por CPF Funcionário", command=lambda: consultar_servicos_db(cpf_funcionario=cpf_funcionario_entry.get()))
    cpf_funcionario_button.place(x=350, y=252)

    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)

def consultar_servicos_db(nome=None, especificacoes=None, id=None, cpf_funcionario=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Servicos WHERE 1=1"
    params = []

    if nome:
        query += " AND Nome = %s"
        params.append(nome)

    if especificacoes:
        query += " AND Especificações = %s"
        params.append(especificacoes)

    if id:
        query += " AND ID_serviço = %s"
        params.append(id)

    if cpf_funcionario:
        query += " AND Cpf_func = %s"
        params.append(cpf_funcionario)

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            messagebox.showinfo("Resultados", f"Serviços encontrados: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhum serviço encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar serviços: {e}")

    finally:
        cursor.close()
        conn.close()
#============Consulta Pagamentos===================
def consultar_pagamentos():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Pagamentos: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos")
    todos_button.place(x=20, y=50)

    id_agendamento_label = Label(RightFrame, text="ID_Agendamento: ", font=("Arial", 14), bg="#FFE5B4")
    id_agendamento_label.place(x=20, y=100)
    id_agendamento_entry = Entry(RightFrame, width=30)
    id_agendamento_entry.place(x=200, y=105)
    id_agendamento_button = ttk.Button(RightFrame, text="Consultar por Agendamento")
    id_agendamento_button.place(x=350, y=102)

    id_label = Label(RightFrame, text="ID: ", font=("Arial", 14), bg="#FFE5B4")
    id_label.place(x=20, y=150)
    id_entry = Entry(RightFrame, width=30)
    id_entry.place(x=200, y=155)
    id_button = ttk.Button(RightFrame, text="Consultar por ID")
    id_button.place(x=350, y=152)

    data_label = Label(RightFrame, text="Data (Ano-Mês-Dia): ", font=("Arial", 14), bg="#FFE5B4")
    data_label.place(x=20, y=200)
    data_entry = Entry(RightFrame, width=30)
    data_entry.place(x=200, y=205)
    data_button = ttk.Button(RightFrame, text="Consultar por Data")
    data_button.place(x=350, y=202)

    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)

    # Configurando ações dos botões
    todos_button.config(command=consultar_pagamentos_db)
    id_agendamento_button.config(command=lambda: consultar_pagamentos_db(id_agendamento=id_agendamento_entry.get()))
    id_button.config(command=lambda: consultar_pagamentos_db(id_pagamento=id_entry.get()))
    data_button.config(command=lambda: consultar_pagamentos_db(data=data_entry.get()))

def consultar_pagamentos_db(id_agendamento=None, id_pagamento=None, data=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Pagamento WHERE 1=1"
    params = []

    if id_agendamento:
        query += " AND ID_Agendamento = %s"
        params.append(id_agendamento)

    if id_pagamento:
        query += " AND ID = %s"
        params.append(id_pagamento)

    if data:
        query += " AND Data = %s"
        params.append(data)

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            # Aqui você pode exibir os resultados em uma nova janela ou em uma tabela
            messagebox.showinfo("Resultados", f"Pagamentos encontrados: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhum pagamento encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar pagamentos: {e}")

    finally:
        cursor.close()
        conn.close()
#============Consulta Agendamentos===================
def consultar_agendamentos():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label = Label(RightFrame, text="Como você deseja consultar Agendamentos: ", font=("Arial", 20), bg="#FFE5B4")
    Consulta_Label.place(x=20, y=10)

    todos_button = ttk.Button(RightFrame, text="Consultar Todos")
    todos_button.place(x=20, y=50)

    # Consultar por Status
    status_label = Label(RightFrame, text="Status: ", font=("Arial", 14), bg="#FFE5B4")
    status_label.place(x=20, y=100)
    status_entry = Entry(RightFrame, width=30)
    status_entry.place(x=200, y=105)
    status_button = ttk.Button(RightFrame, text="Consultar por Status")
    status_button.place(x=360, y=102)

    # Consultar por ID
    id_label = Label(RightFrame, text="ID: ", font=("Arial", 14), bg="#FFE5B4")
    id_label.place(x=20, y=150)
    id_entry = Entry(RightFrame, width=30)
    id_entry.place(x=200, y=155)
    id_button = ttk.Button(RightFrame, text="Consultar por ID")
    id_button.place(x=360, y=152)

    # Consultar por Data
    data_label = Label(RightFrame, text="Data (Ano-Mês-Dia): ", font=("Arial", 14), bg="#FFE5B4")
    data_label.place(x=20, y=200)
    data_entry = Entry(RightFrame, width=30)
    data_entry.place(x=200, y=205)
    data_button = ttk.Button(RightFrame, text="Consultar por Data")
    data_button.place(x=360, y=202)

    # Consultar por Código do Cliente
    cod_cliente_label = Label(RightFrame, text="Código do Cliente: ", font=("Arial", 14), bg="#FFE5B4")
    cod_cliente_label.place(x=20, y=250)
    cod_cliente_entry = Entry(RightFrame, width=30)
    cod_cliente_entry.place(x=200, y=255)
    cod_cliente_button = ttk.Button(RightFrame, text="Consultar por Código do Cliente")
    cod_cliente_button.place(x=360, y=252)

    todos_button.config(command=lambda: consultar_agendamentos_db())
    
    status_button.config(command=lambda: consultar_agendamentos_db(status=status_entry.get()))
    
    id_button.config(command=lambda: consultar_agendamentos_db(id_agendamento=id_entry.get()))
    
    data_button.config(command=lambda: consultar_agendamentos_db(data=data_entry.get()))
    
    cod_cliente_button.config(command=lambda: consultar_agendamentos_db(cod_cliente=cod_cliente_entry.get()))


    # Botão Voltar_Consulta
    Voltar_pgConsulta = ttk.Button(RightFrame, text="Voltar", width=64, command=consultar)
    Voltar_pgConsulta.place(x=130, y=550)
    
def consultar_agendamentos_db(status=None, id_agendamento=None, data=None, cod_cliente=None):
    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM Agendamento WHERE 1=1"
    params = []

    if status:
        query += " AND Status = %s"
        params.append(status)

    if id_agendamento:
        query += " AND Cod_agendamento = %s"
        params.append(id_agendamento)

    if data:
        query += " AND Data = %s"
        params.append(data)

    if cod_cliente:
        query += " AND Cod_Cliente = %s"
        params.append(cod_cliente)

    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if results:
            # Aqui você pode exibir os resultados em uma nova janela ou em uma tabela
            messagebox.showinfo("Resultados", f"Agendamentos encontrados: {results}")
        else:
            messagebox.showinfo("Resultado", "Nenhum agendamento encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar agendamentos: {e}")

    finally:
        cursor.close()
        conn.close()

#=========Configurando botao consulta============
def consultar():
    for widget in RightFrame.winfo_children():
        widget.place_forget()

    Consulta_Label= Label(RightFrame,text="O que você deseja consultar: ",font=("Arial", 20),bg="#FFE5B4")
    Consulta_Label.place(x=20,y=10)

    ConCliente = ttk.Button(RightFrame, text="Clientes", width=32,style="Custom.TButton",command=consultar_clientes)
    ConCliente.place(x=130, y=60)

    ConSeguradora = ttk.Button(RightFrame, text="Seguradoras", width=32,style="Custom.TButton",command=consultar_seguradora)
    ConSeguradora.place(x=130, y=140)

    ConFuncionario = ttk.Button(RightFrame, text="Funcionários", width=32,style="Custom.TButton",command=consultar_funcionarios)
    ConFuncionario.place(x=130, y=220)

    ConServico = ttk.Button(RightFrame, text="Serviços", width=32,style="Custom.TButton",command=consultar_servicos)
    ConServico.place(x=130, y=300)

    ConPagamento = ttk.Button(RightFrame, text="Pagamentos", width=32,style="Custom.TButton",command=consultar_pagamentos)
    ConPagamento.place(x=130, y=380)

    ConAgendamento = ttk.Button(RightFrame, text="Angendamentos", width=32,style="Custom.TButton",command=consultar_agendamentos)
    ConAgendamento.place(x=130, y=460)

    # Botão Voltar página de registro
    Voltar_pgRegistro = ttk.Button(RightFrame, text="Voltar", width=64, command=voltar_Registro)
    Voltar_pgRegistro.place(x=130, y=550)

#Criar janela
jan = Tk()
jan.title("Painel de Registro")
jan.geometry("900x600")
jan.configure(background="gray")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="tim.ico")

#logo
logo= PhotoImage(file="tim.png")

#Frames
LeftFrame =Frame(jan,width=250,height=585,bg=("#FFE5B4"),relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame =Frame(jan,width=640,height=585,bg=("#FFE5B4"),relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame,image=logo, bg="#FFE5B4")
LogoLabel.place(x=20,y=100)

#Nome da empresa

NomeLabel= Label(LeftFrame,text=" Empresa \nFaz-Tudo",font=("Arial", 30),bg="#FFE5B4")
NomeLabel.place(x=40,y=300)

#Botões Cadastro/Consulta

custom_font = font.Font(family="Arial", size=16, weight="normal")

style = ttk.Style()
style.configure("Custom.TButton",font=custom_font,background="#4CAF50",padding=(0,20))

CadastroButton = ttk.Button(RightFrame, text="Cadastrar", width=32, style="Custom.TButton",command=cadastrar)
CadastroButton.place(x=130,y=200)

ConsultaButton= ttk.Button(RightFrame,text="Consultar",width=32,style="Custom.TButton",command=consultar)
ConsultaButton.place(x=130,y=300)

jan.mainloop()