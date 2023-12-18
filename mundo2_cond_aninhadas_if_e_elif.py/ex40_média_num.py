nota1DoAluno = float(input('Digite a nota de matematica: '))
nota2DoAluno = float(input('Digite a nota de portugues: '))
mediaDaNota = (nota1DoAluno + nota2DoAluno) / 2
if mediaDaNota < 5.0:
    print(f'Sua média é {mediaDaNota} portanto está reprovado')
elif mediaDaNota >= 7.0:
    print(f'Sua média é {mediaDaNota}, está aprovado!')
elif mediaDaNota <= 6.9 and mediaDaNota >= 5.0:
    print(f'Sua média é{mediaDaNota} então está de recuperação')

#Aqui estou calculando a media da nota de um aluno e mostrando se ele passou, reprovou ou
#ficou de recuperação. mundo 2 - ex 40