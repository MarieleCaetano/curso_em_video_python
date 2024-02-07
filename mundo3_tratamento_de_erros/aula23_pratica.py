# try: serve para tentar
# except: se der problema - posso usar varios except para ver os mais variados tipos de erro
# else: se não der problema
# finally: vai aparecer independente se deu certo ou não
 #EXEMPLO
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:  #mostra o tipo de erro
    print(f'Infelizmente tivemos um erro classe.. que foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado.')

#-----------------------------------------------

try:
    w = int(input('Numerador: '))
    q = int(input('Denominador: '))
    t = w/q
except (ValueError, TypeError): # se for algum desses dois erros vai printar o print abaixo
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'A causa do erro é {erro.__cause__}')
else:
    print(f'O resultado foi {t:.1f}')
finally:
    print('Volte sempre :)')