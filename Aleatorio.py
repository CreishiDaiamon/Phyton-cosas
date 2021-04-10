import random
import math
from random import choice

Miembros = ["Ricardo", "Sebas", "BA", "Darvin"]
Problemas = [10, 11, 12, 13, 14, 15, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

for x in range( len(Miembros)-1, -1, -1):
    lista =  choice( Miembros)
    print (lista)
    for x in range( len(Miembros)-1, -1, -1):
        if Miembros[x] == lista :
            Miembros.pop(x)
    for x in range( len(Problemas)-1, len(Problemas)-5, -1 ):
        lista =  choice( Problemas)
        print (lista)
        for x in range( len(Problemas)-1, -1, -1):
            if Problemas[x] == lista :
                Problemas.pop(x)
print (Problemas)
