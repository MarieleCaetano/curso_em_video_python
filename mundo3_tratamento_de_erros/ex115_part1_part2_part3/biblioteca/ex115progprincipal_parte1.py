from biblioteca import funcoesdapar1doex115
from  biblioteca import funcaodapar2doex115

from time import sleep

arquivo = 'cursoemvideo.txt'
if funcaodapar2doex115.meuarquivoexiste(arquivo):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado.')

while True:
    funcoesdapar1doex115.cabeçalho('Sistema / arquivo 1.0')
    resp = funcoesdapar1doex115.menu(['Ver pessoas cadastradas', 'cadastro de pessoa', 'Sair do sistema'])
    if resp == 1:
        funcoesdapar1doex115.cabeçalho('\033[35mOpção 1\033[m')
    elif resp == 2:
        funcoesdapar1doex115.cabeçalho('\033[35mOpção 2\033[m')
    elif resp == 3:
        funcoesdapar1doex115.cabeçalho('\033[35mOpção 3, saindo do sistema... Até breve!\033[m')
        break
    else:
        print('\033[31mErro, digite uma opção válida\033[m')
    sleep(1.5)