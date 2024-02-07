def meuarquivoexiste(nome):
    try:
        a = open(nome, 'rt')  #funçao open tenta abrir um arquivo
        a.close() #função close fecha o arquivo
    except FileNotFoundError:     #filenotfounderror é o erro de nao conseguir encontrar o arquivo
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # W - write, T - TEST, + - SE N TIVER UM ARQUIVO DE TEXTO ELE VAI CRIAR UM
        a.close()
    except:
        print('Houve um erro na criação do arquivo')