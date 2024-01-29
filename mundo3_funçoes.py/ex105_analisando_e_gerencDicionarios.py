def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r



resp = notas(9, 6, 5.5, 2.5, 8.4, sit=True)
print(resp)