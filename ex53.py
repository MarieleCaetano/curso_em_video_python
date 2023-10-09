#ler a frase
#frase = str(input('Digite uma frase: '))
#string_sem_espacos = frase.replace(' ', '')
#string_toda_minuscula = string_sem_espacos.lower()

#stringInvertida = string_toda_minuscula[::-1]
#if string_toda_minuscula == stringInvertida:
#        print(f'Sua frase  de trás pra frente fica {stringInvertida}, portanto é um polindromo')


#jeito que o guanabaara fez
frase = str(input('Digite a sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('Não é um palindromo')