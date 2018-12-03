# Fails: 170.py
# Autors : Reinis Lācis
# Apliecības numurs : 181REB265
# Datums: 20181203
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding: utf-8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

# Definejam argumenta x robezhas:
a = 1.1
b = 3.2
k=0
# Apreekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)
# paarbaudam vai dotaja intervaalaa ir saknes:
if ( funa * funb > 0.0):
    print ("Dotajā intervālā [%s, %s] saknju nav"%(a,b))
    sleep(1); exit() #Ziņo uz ekrāna, gaida 1 sec. un darbu pabeidz
else:
    print("Dotajaa intervaalā sakne (s) ir!")
# Definējam precizitāti, ar kādu meklēsim sakni:
deltax = 0.01
#Sašaurinam saknes meklēšanas robežas:
while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
     k=k+1
     b = x
    else:
        a = x
print ("Sakne ir: ", x)
print("funkcijas vērtības šajā punktā ir: ", f(x))
print("intervālu dalīšana uz pusēm: ",k)
