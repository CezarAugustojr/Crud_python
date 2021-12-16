import Listar
import crud



lista = []

usu_correto = 'Atividade3'
sen_correto = '123456'
correto = False
Continuar = True


print('================================================')
print('================================================')
print('================    LOGIN    ===================')
print('=========  Papelaria Boa Esperança   ===========')
print('================================================')

while (correto == False):
    usuario = input('Digite o Usuario: ')
    senha = input('Digite a senha: ')

    if (usuario == usu_correto) and (senha == sen_correto):
        print('Login correto')
        print('')
        print('')

        while(Continuar == True):
            print('================================================')
            print('             Papelaria Boa Esperança            ')
            print('================================================')
            print('')
            print('')
            print('1 - Cadastrar Produtos')
            print('2 - Mostrar todos os Produtos')
            print('3 - Selecionar um Produto especifico')
            print('4 - Alterar Produto')
            print('5 - Excluir Produto')
            print('6 - Sair do Sistema')

            escolha = int(input('Digite a opção desejada: '))

            if(escolha == 1):
                print('Cadastrar Produto: ')
                print('')
                crud.cad(lista)
            elif(escolha == 2):
                verifica = crud.verificar(lista)
                if(verifica == True):
                    print('')
                    Listar.mostralistared(lista)
                else:
                    print("Nenhum produto cadastrado !")
                    print('')
                    menu = input('Digite qualquer tecla para voltar ao menu !')
            elif(escolha == 3):
                verifica = crud.verificar(lista)
                if(verifica == True):
                    print('Selecionar Produto: ')
                    print('')
                    crud.selec(lista)
                else:
                    print("Nenhum produto cadastrado !")
                    print('')
                    menu = input('Digite qualquer tecla para voltar ao menu !')
            elif(escolha == 4):
                verifica = crud.verificar(lista)
                if(verifica == True):
                    print('Alterar Produto: ')
                    print('')
                    crud.Alterar(lista)
                else:
                    print("Nenhum produto cadastrado !")
                    print('')
                    menu = input('Digite qualquer tecla para voltar ao menu !')
            elif(escolha == 5):
                verifica = crud.verificar(lista)
                if(verifica == True):
                    print('Excluir Produto: ')
                    print('')
                    crud.Excluir(lista)
                else:
                    print("Nenhum produto cadastrado !")
                    print('')
                    menu = input('Digite qualquer tecla para voltar ao menu !')
            elif(escolha == 6):
                print('')
                print('Finalizando o Programa')
                Continuar = False
            else:
                print('Opção invalida !')
                print('')

        correto = True
    else:
        print('')
        print('Login incorreto !')
