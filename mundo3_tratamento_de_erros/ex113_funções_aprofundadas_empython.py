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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um numero válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mO Usuario preferiu não digitar nenhum numero válido.\033[m')
            return 0 
        else:
            return n


num = Leiaint('Digite um valor: ')
real = leiafloat('Digite um numero real: ')
print(f'O valor digitado foi {num} e o real foi {real}')