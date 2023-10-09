#ex35 - mundo 1 - aula 10 e ex42 do mundo 2

tr1 = float(input('Digite o tamanho da primeira reta: '))
tr2 = float(input('Digite o tamanho da segunda reta: '))
tr3 = float(input('Digite o tamanho da terceira reta: '))

if (tr1 < tr2 + tr3 and tr2 < tr3 + tr1 and tr3 < tr1 + tr2):
    print('As três retas formam um triangulo ', end='')
    if tr1 == tr2 == tr3:
            print('Equilatero!!!')
    if tr1 != tr2 != tr3 != tr1:
            print('Escaleno!!!')
    else:
            print('Isosceles!!! ')

else:
    print('A soma das restas não formam um triangulo')
