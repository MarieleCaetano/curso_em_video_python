#from math import hypot
#co = float(input("comprimento do cateto oposto: "))
#ca = float(input("comprimento no cateto adjacente: "))
#hi = hypot(co, ca)

#print('nesse caso, a hipotenusa vai medir {}'.format(hi))


import math
ops = float(input("Digite o angulo: "))
ang = math.radians(ops)
seno= float(math.sin(ang))
coss= float(math.cos(ang))
tang= float(math.tan(ang))
print('O angulo que você digitou {}, o seno {:.2f}, cosseno {:.2f} e a tangente {:.2f} são esses respecitvos valores'.format(ang, seno, coss, tang))
