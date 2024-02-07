def Leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro, por favor digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mErro: programa interrompido pelo usuario, digite um numero valido.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[1;32;40mMENU PRINCIPAL\033[m')
    Cw = 1
    for item in lista:
        print(f'\033[33m{Cw}\033[m - \033[34m{item}\033[m')
        Cw += 1
    print(linha())
    opcao = Leiaint('Sua opção: ')
    return opcao