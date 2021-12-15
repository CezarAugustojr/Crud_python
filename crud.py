import Listar

def Alterar(lista):
    loop = True
    p = True
    Listar.mostralistared(lista)
    
    while(loop == True):
    
        escolha = input('Qual opção deseja pesquisar?[N] para o numero do produto, [P] para o nome do produto: ')
        
        if(escolha.upper() == 'N'):
            n = int(input('Qual numero do produto deseja editar ?'))
            posicao = Listar.mostralistacomNumero(lista,n) 
            
            if (posicao >= 0):
                editar = input('O que deseja alterar : ')
                for i in range(0,len(lista[posicao])):
                    if (editar in str(lista[posicao][i])):
                        if ((i == 1) or (i == 2)):
                            while(p == True):
                                des_reg = input('Deseja dar (D)esconto ou (R)eajuste ?')
                                if(des_reg.upper() =='D'):
                                    qtd_des = int(input('Qual a porcentagem que deseja dar de desconto ?'))
                                    res = lista[posicao][i] * qtd_des / 100
                                    
                                    vl_alterar = lista[posicao][i] - res
                                    
                                    lista[posicao][i] = vl_alterar
                                    Listar.mostralistared(lista)
                                    print('')
                                    teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                                    p = False
                                elif(des_reg.upper() == 'R'):
                                    qtd_re = int(input('Qual a porcentagem que deseja dar de reajuste ?'))
                                    res = lista[posicao][i] * qtd_re / 100
                                    
                                    vl_alterar = lista[posicao][i] + res
                                    
                                    lista[posicao][i] = vl_alterar
                                    Listar.mostralistared(lista)
                                    teste = str(input('Digite qualquer tecla para voltar ao menu principal! '))
                                    p = False
                                else: 
                                    print('Opção invalida !')
                                    p = True
                        else:   
                            valor = input('Por qual deseja alterar ?')
                            lista[posicao][i] = valor
                            Listar.mostralistared(lista)
                            teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
            else :
                print('Produto não encontrado !')
            loop = False
        elif(escolha.upper() == 'P'):
            produto = input('Qual produto deseja editar ?')
            posicao = Listar.mostralistacom(lista,produto)
            
            if (posicao >= 0):
                editar = input('O que deseja alterar : ')
                for i in range(0,len(lista[posicao])):
                    if (editar in str(lista[posicao][i])):
                        if ((i == 1) or (i == 2)):
                            while(p == True):
                                des_reg = input('Deseja dar (D)esconto ou (R)eajuste ? ')
                                if(des_reg.upper() =='D'):
                                    qtd_des = int(input('Qual a porcentagem que deseja dar de desconto ?'))
                                    res = lista[posicao][i] * qtd_des / 100
                                    
                                    vl_alterar = lista[posicao][i] - res
                                    
                                    lista[posicao][i] = vl_alterar
                                    Listar.mostralistared(lista)
                                    print('')
                                    teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                                    p = False
                                elif(des_reg.upper() == 'R'):
                                    qtd_re = int(input('Qual a porcentagem que deseja dar de reajuste ?'))
                                    res = lista[posicao][i] * qtd_re / 100
                                    
                                    vl_alterar = lista[posicao][i] + res
                                    
                                    lista[posicao][i] = vl_alterar
                                    Listar.mostralistared(lista)
                                    teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                                    p = False
                                else: 
                                    print('Opção invalida !')
                                    p = True
                        else:   
                            valor = input('Por qual deseja alterar ?')
                            lista[posicao][i] = valor
                            Listar.mostralistared(lista)
                            teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
            else :
                print('Produto não encontrado !')
            loop = False
        else:
            print('Escolha invalida !')
            loop = True 
            
def Excluir(lista):
    excluirloop = True
    loop = True
    p = True
    Listar.mostralistared(lista)
    
    while(loop == True):
    
        escolha = input('Qual opção deseja pesquisar?[N] para o numero do produto, [P] para o nome do produto: ')
        
        if(escolha.upper() == 'N'):
            n = int(input('Qual numero do produto deseja excluir ? '))
            posicao = Listar.mostralistacomNumero(lista,n)
            while(excluirloop == True): 
                if (posicao >= 0):
                    excluir = input("Deseja realmente excluir?[s/n] ")
                    
                    if (excluir.upper() == 'S'):
                        lista.remove(lista[posicao])
                        Listar.mostralistared(lista)
                        teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                        excluirloop = False
                    elif (excluir.upper()=='N'):
                        Listar.mostralistared(lista)
                        teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                        excluirloop = False
                    else:
                        print("Opção invalida !")    
                else :
                    print('Produto não encontrado !')
                loop = False
        elif(escolha.upper() == 'P'):
            produto = input('Qual produto deseja excluir? ')
            posicao = Listar.mostralistacom(lista,produto)
            
            while(excluirloop == True):
                if (posicao >= 0):
                    excluir = input("Deseja realmente excluir?[s/n] ")
                    
                    if (excluir.upper() == 'S'):
                        lista.remove(lista[posicao])
                        Listar.mostralistared(lista)
                        teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                        excluirloop = False
                    elif (excluir.upper(0=='N')):
                        Listar.mostralistared(lista)
                        teste = str(input('Digite qualquer tecla para voltar ao menu principal !'))
                        excluirloop = False
                        
                    else:
                        print("Opção invalida !")
                else :
                    print('Produto não encontrado !')
            else :
                print('Produto não encontrado !')
            loop = False
        else:
            print('Escolha invalida !')
            loop = True    

def verificar(lista):
    for i in range(len(lista)):
        if(i>=0):
            return True
    return False
            
            
def cad(lista):
    erro = False
    while(erro == False):
        produto = input('Produto: ')
        quantidade = input('Quantidade: ')
        try:
            quantidade = int(quantidade)
        except:
            erro = True
        valor = input('Valor: ')
        try:
            valor = float(valor)
        except:
            erro = True
        cor = input('Cor: ')
        fabricante = input('Fabricante: ')
        modelo = input("Modelo: ")
        estoque = input('Já possui no Estoque[s]\[n]: ')
        if(estoque.upper() == 'S'):
            estoque = True
        elif(estoque.upper() == 'N'):
            estoque = False
        else:
            erro = True
        print('')
        if(erro == False):
            lista.append([produto,quantidade,valor,cor,fabricante,modelo,estoque])
            Listar.mostralistared(lista)
            erro = True
        else:
            print("Cadastro invalido !")
            menu = input('Digite qualquer tecla para voltar ao menu !')


def selec(lista):
    loop = True
    p = True
    Listar.mostralistared(lista)
    
    while(loop == True):
        
        escolha = input('Qual produto deseja pesquisar: [N] para o numero do produto, [P] para o nome do produto: ')
        
        if(escolha.upper() == 'N'):
            n = int(input('Digite o Numero do produto que deseja selecionar: '))
            print('')
            posicao = Listar.mostralistacomNumero(lista,n)
            menu = input('digite qualquer tecla para voltar')
            loop = False
        elif(escolha.upper() == "P"):
            produto = input('Digite o nome do Produto que deseja selecionar: ')
            print('')
            posicao = Listar.mostralistacom(lista,produto)
            menu = input('digite qualquer tecla para voltar')
            loop = False
        else:
            print('Escolha invalida !')    