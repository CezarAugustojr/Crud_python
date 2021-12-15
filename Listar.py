def mostralistared(lista):

    print('N°       Nome          QTD        VALOR')
    print('=======================================')
    for i in range (len(lista)):
        print(i,'      ',lista[i][0],'       ',lista[i][1],'       ',lista[i][2])
        
    print('')    
def mostralistacom(lista,produto):
    print('Nome          QTD          VALOR          COR          FAB          MOD        ESTQ        ')
    print('===========================================================================================')
    for c in range(len(lista)):
        if(produto in lista[c][0]):
            print(lista[c][0],'        ',lista[c][1],'        ',lista[c][2],'        ',lista[c][3],"        ",lista[c][4],"        ",lista[c][5],"        ",lista[c][6])
            print('')
            
            return c
    return -1
    
def mostralistacomNumero(lista,n):
    
    print('Nome          QTD          VALOR          COR          FAB          MOD        ESTQ        ')
    print('===========================================================================================')
    print(lista[n][0],'        ',lista[n][1],'        ',lista[n][2],'        ',lista[n][3],"        ",lista[n][4],"        ",lista[n][5],"        ",lista[n][6])
    print('')
    
    return n

def selec(lista):
    print('=================================================================')
    for n in range(len(lista,)):
        print(n,'       ',lista[n][0],'       ',lista[n][1],'       ',lista[n][2])    
        print('')
        
