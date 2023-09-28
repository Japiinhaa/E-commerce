from classes import *
import os

loja = Loja("E-commerce", "Rua Alameda Santos, 1293 - Jardim Paulista, São Paulo - SP, 01419-001")
admin = Admin("admin", "123")


def main():
    while True:
        print("--------------------------------Bem vindo ao E-commerce--------------------------------")

        print("[1] - Logar como cliente\n[2] - Logar como administrador\n[3] - Sair")
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                os.system("clear")
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
                            os.system("clear")
                            os.system("pause")
                            break
                        case 2:
                            print("Comprando produtos...")
                            admin.listarProdutos()
                            produto = input("Digite o nome do produto que deseja comprar: ")
                            if produto in produtos:
                                print("Produto comprado com sucesso!")
                                os.system("clear")
                                os.system("pause")
                            else:
                                print("Produto não encontrado!")
                                print("Produto comprado com sucesso!")
                                os.system("clear")
                                os.system("pause")
                            break
                        case 3:
                            print("Saindo...")
                            os.system("clear")
                            os.system("pause")
                            break
                        case _:
                            print("Opção inválida!")
                            os.system("clear")
                            os.system("pause")
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
                            os.system("clear")
                            os.system("pause")
                            break
                        case 2:
                            print("Listando produtos...")
                            admin.listarProdutos()
                            os.system("clear")
                            os.system("pause")
                            break
                        case 3:
                            print("Cadastrando cliente...")
                            admin.cadastrarCliente()
                            os.system("clear")
                            os.system("pause")
                            break
                        case 4:
                            print("Cadastrando produto...")
                            admin.cadastrarProduto(produto)
                            os.system("clear")
                            os.system("pause")
                            break
                        case 5:
                            print("Excluindo cliente...")
                            admin.excluirCliente()
                            os.system("clear")
                            os.system("pause")
                            break
                        case 6:
                            print("Excluindo produto...")
                            admin.excluirProduto(produto)
                            os.system("clear")
                            os.system("pause")
                            break
                        case 7:
                            print("Saindo...")
                            os.system("clear")
                            os.system("pause")
                            break
                        case _:
                            print("Opção inválida!")
                            os.system("clear")
                            os.system("pause")
                            break
                else:
                    print("Usuário ou senha incorretos!")
                    os.system("clear")
                    os.system("pause")
                    break
main()