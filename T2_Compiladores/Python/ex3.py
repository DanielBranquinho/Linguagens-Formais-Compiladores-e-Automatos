#####################################################
## ECM253 – Linguagens Formais, Autômatos e Compiladores - Trabalho 02
## Exercício 3

##Integrantes:
## Carolina de Carvalho Gutierrez - RA: 18.00576-4
## Daniel Branquinho Gomes        - RA: 18.02617-6
## Gabriel Gomes B. S.            - RA: 18.00947-6
## Felipe Ros Pegini              - RA: 18.00232-3

## Importando pathlib
from pathlib import Path


## Usuário escolhe digitar ou utilizar uma cadeia como exemplo
## Send os exemplos iguais aos do documento base para execução do programa
def getInputs():
    global originalChain1
    print('Escolha um automato:\n1 - Automato 1 Ou digite "s" para sair.')
    usrAut = input("Digite sua opcao: ")
    if not usrAut == 's':
        absPath = getAbsPath('Automato {}'.format(usrAut))
        aut = getAut(absPath)
        print("Deseja digitar ou importar a cadeia?")
        usrChain = input("Digite sua opcao [d/i]: ")
        if usrChain == 'd':
            chain = input("Digite a cadeia, com cada elemento separado por  ',': ").split(',')
            originalChain = chain.copy()
        elif usrChain == 'i':
            print("""Exemplos das cadeias:
                              1 = [0 0 0 0]
                              2 = [0 0 0 1 0 1 0 1 0 1 0]
                              3 = [1 0]
                              4 = [1 1 1 0]
                              5 = [1 0 a 1]""")

            numChain = int(input("Digite o numero da cadeia [1,2,3,4,5]: "))
            chain = getChain(absPath, numChain)
            originalChain = chain.copy()
        if usrAut == '5':
            originalChain = chain.copy()
            chain = convertIntToN(chain)
    else:
        aut = 's'
        chain = []
        originalChain = chain.copy()
    return (aut, chain)

## Convertendo chain number para "n"
def convertIntToN(lista):
    for i in range(len(lista)):
        try:
            int(lista[i])
        except:
            pass
        else:
            lista[i] = 'n'
    print(lista)
    return lista  
             
## Mostra o automato exemplo como dicionário
def showAut(aut):
    print('aut :', aut)
    print('    states :', aut['states'])
    print('    iniState :', aut['iniState'])
    print('    finStates :', aut['finStates'])
    print('    values :', aut['values'])
    print('    deltas :', aut['deltas'])

## Função para printar as cadeias
def showChain(chain):
    print('chain :', chain)

## Pega o Path absoluto do diretório do automato
def getAbsPath(dir):
    absPath = str(Path(__file__).parent.parent) + "\\Txt\\" + dir + '\\'
    return absPath

## Importa um automato de um arquivo .txt
def getAut(absPath):
    with open(absPath + 'automato.txt') as file:
        dictionary = eval(file.read())
        return dictionary
        
## Importa uma cadeia exemplo de um .tx
def getChain(absPath, num):
    with open(absPath + 'chain%i.txt' % num) as file:
        lista = eval(file.read())
        lista = [str(step) for step in lista]
        return lista

## Roda o automato utilizando uma dada cadeia
def simulate(aut, chain):
    print('Current state (Cur)\tValue (Val)\tNext state(Nex)')
    print('Cur\tVal\tNex')
    print(19 * '-')
    output = ''
    curState = aut['iniState']
    accept = False
    while len(chain) > 0:
        value = chain.pop(0)
        interfaceText = '%i\t%s\t' %(curState, value)


        if value not in aut['values']:
            chain.insert(0, value)
            output = 'ERRO: O valor %s nao pertence ao alfabeto do automato.' % value
            break
        if curState not in aut['states']:
            output = 'ERRO: O estado %i nao pertence ao conjunto de estados do automato.' % curState
            break


        try:
            curState = aut['deltas'][(curState, value)]
        except:
            output = 'Nao foi possivel realizar a transicao do estado %i com o valor %s.' % (curState, value)
            break
        else:
            interfaceText += str(curState)
            print(interfaceText)
    

    if curState in aut['finStates'] and len(chain) == 0:
        accept = True
    if accept:
        output = 'A cadeia %s foi ACEITA pelo automato.' % originalChain
    else:
        output = 'A cadeia %s foi REJEITADA pelo automato.' % originalChain
    
    return output


#####-Main-#####
## Finaização do menu programado
originalChain = []

while True:
    (aut, chain) = getInputs()
    if aut == 's':
        print('Fechando o programa')
        break
    else:
        print('Cadeia digitada:', chain)
        output = simulate(aut, chain.copy())
        print(output)
        input('Aperte ENTER para continuar')
    print('\n' + 19 * '*' + '\n')