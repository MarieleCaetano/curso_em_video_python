from datetime import date
print('-'*30)
anodenasc = int(input('Digite seu ano de nascimento: '))
print('-'*30)

def voto(* num):
    dia_atual = date.today()
    anoAtual = dia_atual.year
    sub = anoAtual - anodenasc
    num = sub

    if num >= 16 and num < 18 or num > 65:
        print('='*40)
        print(f'A idade é de {num} e o voto é opcional')  
        print('='*40)
           
    elif num >= 18:
        print('='* 40)
        print(f'A idade é de {num} e o voto passa a ser obrigatorio')
        print('='* 40)

    elif num < 16:
        print('='*40)
        print(f'A idade é de {num} e você não precisa votar ainda')
        print('='*40)
        


#prog principal
voto(anodenasc)
