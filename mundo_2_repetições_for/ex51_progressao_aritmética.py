#primeiro termo: 1  e a razão:2 


termo = int(input('Digite o seu numero inicial: '))
razão = int(input('Digite a sua razão: '))
vezes = int(input('Até quantos numeros você quer ver? '))
soma = 0
quantoselem = termo + (vezes-1)
elem = quantoselem + 1

for var in range(termo, elem, razão):
    print(var)
    soma= soma+var