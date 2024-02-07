frase = ''
contador = 0
frase_eh_invalida = False
frase = (str(input('Digite sua expressão: ')))

for c in frase:
    if c == '(':
        contador += 1
    if c == ')':
        contador -= 1

    if contador < 0:
        frase_eh_invalida = True
        break


if frase_eh_invalida:
    print('Sua expressão é invalida, você fechou parenteses antes de abrir')
elif contador != 0:
    print('expressão invalida')
else:
    print('Sua expressão é valida')

# jeito que o guanabara fez
    
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')
    


