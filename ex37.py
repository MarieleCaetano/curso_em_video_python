#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de 
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero inteiro: '))
basedeconversão = input('escolha a base de conversão, 1 para binario, 2 para octal e 3 para hexadecimal: ')
    
if basedeconversão == '1':
    print(f'O numero que você digitou em binario fica {bin(numero).replace("0b", "")}')

elif basedeconversão == '2':
    print(f'O numero que você digitou, em octal fica {oct(numero)}')

elif basedeconversão == '3':
    print(f'O numero que você digitou em hexadecimal fica {hex(numero)}')

else:
    print('Opção invalida, tente novamente')
    