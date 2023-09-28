from classes import *
import os

loja = Loja("E-commerce", "Rua Alameda Santos, 1293 - Jardim Paulista, São Paulo - SP, 01419-001")
admin = Admin("admin", "123")
cliente = Cliente(None, None, None, None)


def main():
    while True:
        print("--------------------------------Bem vindo ao E-commerce--------------------------------")

        print("[1] - Logar como cliente\n[2] - Logar como administrador\n[3] - Sair")
        opcao = int(input("Digite a opção desejada: "))
        match opcao:
            case 1:
                if not clientes:
                    print("Não há clientes cadastrados!")
                    os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
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
                                os.system("pause")
                                os.system("cls")
                                break
                            case 2:
                                print("Comprando produtos...")
                                admin.listarProdutos()
                                produto = input("Digite o nome do produto que deseja comprar: ")
                                if produto in produtos:
                                    print("Produto comprado com sucesso!")
                                    os.system("pause")
                                    os.system("cls")
                                else:
                                    print("Produto não encontrado!")
                                    print("Produto comprado com sucesso!")
                                    os.system("pause")
                                    os.system("cls")
                                break
                            case 3:
                                print("Saindo...")
                                os.system("pause")
                                os.system("cls")
                                break
                            case _:
                                print("Opção inválida!")
                                os.system("pause")
                                os.system("cls")
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
                            admin.listarClientes(clientes)
                            os.system("pause")
                            os.system("cls")
                            break
                        case 2:
                            print("Listando produtos...")
                            admin.listarProdutos(produtos)
                            os.system("pause")
                            os.system("cls")
                            break
                        case 3:
                            print("Cadastrando cliente...")
                            admin.cadastrarCliente()
                            print("Cadastrando um carrinho ao cliente...")
                            x = input("Digite o nome do cliente que deseja cadastrar um carrinho: ")
                            if x in clientes:
                                cliente.getClientenome(x).cadastrarCarrinho(dono = cliente.getClientenome(x), produtos = None, quantide = None)
                                print("Carrinho cadastrado com sucesso!")
                            else:
                                print("Cliente não encontrado!")
                            os.system("pause")
                            os.system("cls")
                            break
                        case 4:
                            print("Cadastrando produto...")
                            admin.cadastrarProduto(produto)
                            os.system("pause")
                            os.system("cls")
                            break
                        case 5:
                            print("Excluindo cliente...")
                            admin.excluirCliente()
                            os.system("pause")
                            os.system("cls")
                            break
                        case 6:
                            print("Excluindo produto...")
                            admin.excluirProduto(produto)
                            os.system("pause")
                            os.system("cls")
                            break
                        case 7:
                            print("Saindo...")
                            os.system("pause")
                            os.system("cls")
                            break
                        case _:
                            print("Opção inválida!")
                            os.system("pause")
                            os.system("cls")
                            break
                else:
                    print("Usuário ou senha incorretos!")
                    os.system("cls")
                    os.system("pause")
                    break
main()