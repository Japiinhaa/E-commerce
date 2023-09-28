from classes import *

loja = Loja("E-commerce", "Rua Alameda Santos, 1293 - Jardim Paulista, São Paulo - SP, 01419-001")
admin = Admin("admin", "123")


def main():
    while True:
        print("--------------------------------Bem vindo ao E-commerce--------------------------------")

        print("[1] - Logar como cliente\n[2] - Logar como administrador\n[3] - Sair")
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                print("Logando como cliente...")
                usuario = input("Digite o nome de usuário: ")
                senha = input("Digite a senha: ")
                if usuario == cliente.getClientenome() and senha == cliente.getClientesenha():
                    print("Bem vindo, " + cliente.getClientenome() + "!")
                    print("[1] - Listar produtos\n[2] - Comprar produtos\n[3] - Sair")
                    opcao = int(input("Digite a opção desejada: "))
                    match opcao:
                        case 1:
                            print("Listando produtos...")
                            admin.listarProdutos()
                            break
                        case 2:
                            print("Comprando produtos...")
                            admin.listarProdutos()
                            produto = input("Digite o nome do produto que deseja comprar: ")
                            if produto in produtos:
                                print("Produto comprado com sucesso!")
                            else:
                                print("Produto não encontrado!")
                            print("Produto comprado com sucesso!")
                            break
                        case 3:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida!")
                            break
                else:
                    print("Usuário ou senha incorretos!")
                    break

            case 2:
                print("Logando como administrador...")
                usuario = input("Digite o nome de usuário: ")
                senha = input("Digite a senha: ")
                if usuario == admin.getAdminnome() and senha == admin.getAdminsenha():
                    print("Bem vindo, " + admin.getAdminnome() + "!")
                    print("[1] - Listar clientes\n[2] - Listar produtos\n[3] - Cadastrar cliente\n[4] - Cadastrar produto\n[5] - Excluir cliente\n[6] - Excluir produto\n[7] - Sair")
                    opcao = int(input("Digite a opção desejada: "))
                    match opcao:
                        case 1:
                            print("Listando clientes...")
                            admin.listarClientes()
                            break
                        case 2:
                            print("Listando produtos...")
                            admin.listarProdutos()
                            break
                        case 3:
                            print("Cadastrando cliente...")
                            admin.cadastrarCliente()
                            break
                        case 4:
                            print("Cadastrando produto...")
                            admin.cadastrarProduto(produto)
                            break
                        case 5:
                            print("Excluindo cliente...")
                            admin.excluirCliente()
                            break
                        case 6:
                            print("Excluindo produto...")
                            admin.excluirProduto(produto)
                            break
                        case 7:
                            print("Saindo...")
                            break
                        case _:
                            print("Opção inválida!")
                            break
                else:
                    print("Usuário ou senha incorretos!")
                    break







main()