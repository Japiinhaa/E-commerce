from typing import Any
clientes = []
produtos = []
admins = []


class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def cadastrarAdmin(self, admin):
        admin.setAdminnome(input("Digite o nome do admin: "))
        admin.setAdminsenha(input("Digite a senha do admin: "))
        admin.append(admins)
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

    def cadastrarCliente(self, cliente):
        cliente.setClientenome(input("Digite o nome do cliente: "))
        cliente.setClienteCPF(input("Digite o CPF do cliente: "))
        cliente.setClienteendereco(input("Digite o endereço do cliente: "))
        cliente.setClientesenha(input("Digite a senha do cliente: "))
        cliente.append(clientes)
        return cliente
    
    def excluirCliente(self, cliente):
        cliente = input("Digite o nome do cliente que deseja excluir: ")
        cliente.pop(clientes)
        return cliente
    
    def cadastrarProduto(self, produto):
        produto.setProdutonome(input("Digite o nome do produto: "))
        produto.setProdutopreco(input("Digite o preço do produto: "))
        produto.setProdutodescricao(input("Digite a descrição do produto: "))
        produto.append(produtos)
        return produto
    
    def excluirProduto(self, produto):
        produto = input("Digite o nome do produto que deseja excluir: ")
        produto.pop(produtos)
        return produto
    
    def listarClientes():
        for i in clientes:
            print(i)
        
    def listarProdutos():
        for i in produtos:
            print(i)

    def excluirAdmin(self, admin):
        admin = input("Digite o nome do admin que deseja excluir: ")
        admin.pop(admins)
        return admin