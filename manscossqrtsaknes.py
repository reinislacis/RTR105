# fails : 170.py
# autors : Reinis Laacis
# apliecības numurs : 181REB265
# datums : 28 12 2018
# sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding : tf -8 -*-
from math import cos, sqrt, fabs
from time import sleep

def f(x):
    return cos(sqrt(x))

#definejam argumenta x robezhas:
a = 1.1
b = 3.2 

# Aprekjinam argumenta x robezhas:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dtotajaa intervaalaa ir saknes:
if (funa * funb > 0.0):
    print("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()    # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print ("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam precizitaati, ar kaadu mekleesim sakni:
deltax = 0.01
# sashaurinam saknes mekleeshanas robezhas:
while (fabs (b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b=x
    else:
        a=x

print ("Sakne ir: ", x)
