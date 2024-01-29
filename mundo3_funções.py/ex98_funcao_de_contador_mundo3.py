from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} pulando de {passo}')
    sleep(1.5)
    if inicio < fim:
        contagem= inicio
        while contagem <= fim:
            print(f'{contagem} ', end='', flush=True)
            sleep(0.5)
            contagem += passo
        print('Fim')
    else:
        contagem = inicio
        while contagem >= fim:
            print(f'{contagem} ', end='', flush=True) #flush=True é usado junto ao sleep para o delei
            # funcionar em prints
            sleep(0.5)
            contagem -= passo
        print('Fim')

#programa principal
contador(1,10,1)
contador(10,0,2)
print('='*30)
print('Agora é sua vez de personalizar a contagem!')
inic = int(input('Inicio: '))
f = int(input('Fim:       '))
pa = int(input('Passo:    '))
contador(inic, f, pa)
