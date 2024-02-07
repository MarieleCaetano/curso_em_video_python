def fatorial(num = 1, show = False):
    """"
     -> Mostra o fatorial de um numero
    :param num: numero a ser mostrado o fatorial
    :param show true: para mostrar todo o processo fatorial do num            
    :param show false: mostra somente o fatorial do numero           
    :return: o valor num
    
    
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end='')
        f *= c
    return f
    


print(fatorial(12, show=True))
