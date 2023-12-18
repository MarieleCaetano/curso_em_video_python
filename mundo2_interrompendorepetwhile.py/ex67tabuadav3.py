tabuada = 1
while True:
    tabuada = int(input("digite um numero  "))
    if tabuada < 0:
        break
    for c in range (0, 11):
        print(f'{tabuada} X {c} = {tabuada*c}')
print('Fim do programa')