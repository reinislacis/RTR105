In [1]: def thing():
   ...:     print('hello')
   ...:     print('fun')
   ...: thing()
   ...: print('zip')
   ...: thing()
   ...: 
hello
fun
zip
hello
fun

In [2]: big=max('hello world')

In [3]: print(big)
w

In [4]: 

In [4]: big=max('hello world')

In [5]: print(big)
w

In [6]: tiny=min('hello world')

In [7]: print(tiny)
 

In [8]: 

In [8]: x=5

In [9]: print('hello')
hello

In [10]: def print_lyrics():
    ...:     print('man garšo ēst')
    ...:     print('ha ha ha')
    ...: print('yo')
    ...: x=x+2
    ...: print(x)
    ...: 
yo
7

In [11]: print(lyrics)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-11-edd26609e200> in <module>()
----> 1 print(lyrics)

NameError: name 'lyrics' is not defined

In [12]: print(lyrics):
  File "<ipython-input-12-d8e4f50df2f9>", line 1
    print(lyrics):
                  ^
SyntaxError: invalid syntax


In [13]: 

In [13]: print_lyrics()
man garšo ēst
ha ha ha

In [14]: def greet(lang):
    ...:     if lang=='es':
    ...:         print('hola')
    ...:     elif lang=='fr':
    ...:         print('bonjiur')
    ...:     else:
    ...:         print('hello')
    ...:         

In [15]: greet('en')
hello

In [16]: greet('es')
hola

In [17]: greet('fr')
bonjiur

In [18]: def greet():
    ...:     return'hello'
    ...: print(greet(),'Reini')
    ...: 
hello Reini

In [19]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...: elif lang=='fr':
  File "<ipython-input-19-302f7fc6608f>", line 4
    elif lang=='fr':
       ^
SyntaxError: invalid syntax


In [20]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...: elif lang=='fr':
  File "<ipython-input-20-302f7fc6608f>", line 4
    elif lang=='fr':
       ^
SyntaxError: invalid syntax


In [21]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...: elif lang == 'fr':
  File "<ipython-input-21-1080acc431ec>", line 4
    elif lang == 'fr':
       ^
SyntaxError: invalid syntax


In [22]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...:     elif lang=='fr':
    ...:         return('sveiki')
    ...:     else:
    ...:         return('hello')
    ...:     

In [23]: print(greet('en'),Gleen)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-23-438c32902364> in <module>()
----> 1 print(greet('en'),Gleen)

NameError: name 'Gleen' is not defined

In [24]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...:     elif lang=='fr':
    ...:         return('sveiki')
    ...:     else:
    ...:         return('hello')
    ...:     print(greet('en'),'Gleen')
    ...:     

In [25]: def greet(lang):
    ...:     if lang=='es':
    ...:         return'hola'
    ...:     elif lang=='fr':
    ...:         return('sveiki')
    ...:     else:
    ...:         return('hello')
    ...:     print(greet('en'),'Gleen')
    ...:   

In [26]: print(greet('en'),'Gleen')
hello Gleen

In [27]: def addtwo(a,b):
    ...:     added=a+b
    ...:     return added
    ...: 

In [28]: x=addtwo(3,5)

In [29]: print(x)
8

In [30]: exit()
user@epk428-19:~/RTR105$ 

