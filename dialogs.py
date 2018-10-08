#!/usr/bin/python
#-*- coding: utf-8 -*-

a = input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. python'ā visi input rezultāti ir ar str datu tipu
# tāpēc ievadītā lieluma datu tips vēlāk ir pāparveido
a = int(a)

# python valoda balstās uz C valodas => print strādā līdzīgi printf
# https://www.cplusplus.com/reference/cstdio/printf/
print("liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

