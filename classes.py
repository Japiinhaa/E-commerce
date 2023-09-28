from typing import Any
clientes = []
produtos = []
admins = []

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def cadastrarAdmin(self, admin):
        admin = Admin (nome = input("Digite o nome do admin: "), senha = input("Digite a senha do admin: "))
        admins.append(admin)
        return admin

class Cliente:
    def __init__(self, nome, cpf, endereco, senha):
        self.nome = None
        self.cpf = None
        self.endereco = None
        self.telefone = None
        self.email = None
        self.senha = None
    
    def getClientenome(self):
        return self.nome
    
    def setClientenome(self, nome):
        self.nome = nome

    def getClienteCPF(self):
        return self.cpf
    
    def setClienteCPF(self, cpf):
        self.cpf = cpf

    def getClienteendereco(self):
        return self.endereco
    
    def setClienteendereco(self, endereco):
        self.endereco = endereco

    def getClientesenha(self):
        return self.senha
    
    def setClientesenha(self, senha):
        self.senha = senha

    def getCarrinho(self):
        return self.carrinho
    
    def setCarrinho(self, carrinho):
        self.carrinho = carrinho

    def cadastrarCarrinho(carrinho):
        carrinho = Carrinho(dono = input("Digite o nome do dono do carrinho: "), produto = input("Digite o nome do produto: "), quantidade = input("Digite a quantidade do produto: "))
        return carrinho

class Carrinho:
    def __init__(self, dono, produto, quantidade):
        self.dono = None
        self.produto = None
        self.quantidade = None

    def getCarrinhodono(self):
        return self.dono
    
    def setCarrinhodono(self, dono):
        self.dono = dono

    def getCarrinhoproduto(self):
        return self.produto
    
    def setCarrinhoproduto(self, produto):
        self.produto = produto

    def getCarrinhoquantidade(self):
        return self.quantidade
    
    def setCarrinhoquantidade(self, quantidade):
        self.quantidade = quantidade

class Produtos:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def getProdutonome(self):
        return self.nome
    
    def setProdutonome(self, nome):
        self.nome = nome

    def getProdutopreco(self):
        return self.preco
    
    def setProdutopreco(self, preco):
        self.preco = preco

    def getProdutodescricao(self):
        return self.descricao
    
    def setProdutodescricao(self, descricao):
        self.descricao = descricao

class Admin(Cliente, Produtos, Loja):
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def getAdminnome(self):
        return self.nome
    
    def setAdminnome(self, nome):
        self.nome = nome

    def getAdminsenha(self):
        return self.senha
    
    def setAdminsenha(self, senha):
        self.senha = senha

    def cadastrarCliente(cliente):
        cliente = Cliente (nome = input("Digite o nome do cliente: "), cpf = input("Digite o CPF do cliente: "), endereco = input("Digite o endereço do cliente: "), senha = input("Digite a senha do cliente: "))
        clientes.append(cliente)
        return cliente
    
    def excluirCliente(cliente):
        cliente = input("Digite o nome do cliente que deseja excluir: ")
        clientes.pop(cliente)
        return cliente
    
    def cadastrarProduto(produto):
        produto = Produtos (nome = input("Digite o nome do produto: "), preco = input("Digite o preço do produto: "), descricao = input("Digite a descrição do produto: "))
        produtos.append(produto)
        return produto
    
    def excluirProduto(produto):
        produto = input("Digite o nome do produto que deseja excluir: ")
        produtos.pop(produto)
        return produto
    
    def listarClientes():
        if not clientes:
            print("Não há clientes cadastrados!")
        else:
            for i in clientes:
                print(i)

    def listarProdutos():
        if not produtos:
            print("Não há produtos cadastrados!")
        else:
            for i in produtos:
                print(i)

    def excluirAdmin(self, admin):
        admin = input("Digite o nome do admin que deseja excluir: ")
        admin.pop(admins)
        return admin