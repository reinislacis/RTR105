# -*- coding: utf-8 -*-
   ...: from math import cos
   ...: from math import sqrt
   ...: def mans_cossqrt(x):
   ...:     k = 0
   ...:     a = (-1)**0*x**0/(1)
   ...:     S = a
   ...:     print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))
   ...:     while k < 500:
   ...:         k = k + 1
   ...:         R = (-1)*x/((2*k)*(2*k-1))
   ...:         a = a * R
   ...:         S = S + a
   ...:         if k == 499:
   ...:              print("Izdruka no liet.f. a499 = %6.2f S499 = %6.2f"%(a,S))
   ...:     print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
   ...:     print("Izdruka no liet.f. Beigas!")
   ...:     return S
   ...: x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
   ...: y = cos(sqrt(x))
   ...: print("standarta cossqrt(%.2f) = %6.2f"%(x,y))
   ...: yy = mans_cossqrt(x)
   ...: b=u"\u221E"
   ...: print("mans cossqrt(%.2f) = %6.2f"%(x,yy))
   ...: print(" ")
   ...: print("                 500")
   ...: print("                _____")
   ...: print("               \         k    k")
   ...: print("                \    (-1) * x ")
   ...: print("cos(sqrt(%.2f/2))=>  __________            D.a. -%s < x < %s "%(x,b,b))
   ...: print("                /                    ")
   ...: print("               /____ (2*k)! ")
   ...: print("                k=0")
   ...: print(" ")
   ...: print("                                1     1")
   ...: print("                            (-1)  * x ")
   ...: print("rekurences reizinātājs: _________________")
   ...: print("                                         ")
   ...: print("                         (2*k-1) * (2*k) ")
   ...: 
