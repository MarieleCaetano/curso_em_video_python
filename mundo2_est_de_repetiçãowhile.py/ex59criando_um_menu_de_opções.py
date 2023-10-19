from time import sleep
import random

opções_do_menu = 0
while opções_do_menu != 5:
    primeirovalor_escolhido = int(input('\033[94mDigite o 1º valor: '))
    sleep(1)
    segundovalor_escolhido = int(input('\033[94mDigite o 2º valor: '))
    sleep(1)
    opções_do_menu = int(input("""----ESCOLHA UMA DAS OPÇÕES ------- 
.....[1] Somar 
.....[2] multiplicar 
.....[3] maior 
.....[4]novos numeros 
.....[5] para sair do programa:\n"""))
    if opções_do_menu == 1:
        resultadodasoma = primeirovalor_escolhido + segundovalor_escolhido
        print(f'O resultado da soma dos dois valores digitados é {primeirovalor_escolhido} + {segundovalor_escolhido} = {resultadodasoma}')
    elif opções_do_menu == 2:
        resultadodamultiplicação = primeirovalor_escolhido * segundovalor_escolhido
        print(f'O resultado da multiplicação dos dois numeros é {primeirovalor_escolhido} X {segundovalor_escolhido} = {resultadodamultiplicação}')
    elif opções_do_menu == 3:
        if primeirovalor_escolhido > segundovalor_escolhido:
            print(f'O maior valor digitado é o primeiro valor, que é {primeirovalor_escolhido}')
        elif segundovalor_escolhido > primeirovalor_escolhido:
            print(f'O segundo valor digitado é o maior, que é o numero {segundovalor_escolhido}')
        else:
            print('Os dois valores são iguais')
    elif opções_do_menu == 4:
        num = (random.randint(0,500))
        num2 = (random.randint(0,500))
        print(f'Os dois novos numeros que o computador escolheu para você são {num} e {num2}')
    else:
        print('Opção invalida, tente novamente')

print('Finalizando..')
sleep (1)
print('---Programa encerrado!!! Volte sempre---''')
