Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=12,2
>>> y=14
>>> print(123)
123
>>> print(98,6)
(98, 6)
>>> print("Hello world")
Hello world
>>> print(x)
(12, 2)
>>> print(y)
14
>>> print(x)
(12, 2)
>>> spams=33
>>> spams
33
>>> 23spam
SyntaxError: invalid syntax
>>> SPAM44

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    SPAM44
NameError: name 'SPAM44' is not defined
>>> SPAM

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    SPAM
NameError: name 'SPAM' is not defined
>>> spam

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
>>> SPAMS=44
>>> SPAMS
44
>>> a=1
>>> b=2.50
>>> c=a*b
>>> print(c)
2.5
>>> hours=35,5
>>> rate=12,50
>>> pay=hours*rate

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    pay=hours*rate
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> pay=hours*rate

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    pay=hours*rate
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> haours=12.5
>>> rate=4.4
>>> pay=hours*pay

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pay=hours*pay
NameError: name 'pay' is not defined
>>> pay=hours*rate

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    pay=hours*rate
TypeError: can't multiply sequence by non-int of type 'float'
>>> x=2
>>> x=x+2
>>> print(x)
4
>>> x=3.9*x*(1-x)
>>> print(x)
-46.8
>>> xx=2
>>> xx=xx+2
>>> print(xx)
4
>>> zz=xx/1000
>>> print(zz)
0
>>> jj=23
>>> kk=jj%5
>>> print(kk)
3
>>> print(4**3)
64
>>> x=1+2*3-4/5**6
>>> print(x)
7
>>> ddd=1+4
>>> print(ddd)
5
>>> eee='hello''+ 'there'
SyntaxError: invalid syntax
>>> print(eee)

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(eee)
NameError: name 'eee' is not defined
>>> print(float(99)+100)
199.0
>>> i=42
>>> f=float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(9/2)
4
>>> print(10/2)
5
>>> sval='123'
>>> type(sval)
<type 'str'>
>>> print(sval+1)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(sval+1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival=int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival+1)
124
>>> nam=input('who are you?)
	  
SyntaxError: EOL while scanning string literal
>>> nam=input('who are you?')
who are you?print('Welcom' nam)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    nam=input('who are you?')
  File "<string>", line 1
    print('Welcom' nam)
        ^
SyntaxError: invalid syntax
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> nam

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    nam
NameError: name 'nam' is not defined
>>> nam=input('who are you?')
who are you?print('Welcom',nam)

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    nam=input('who are you?')
  File "<string>", line 1
    print('Welcom',nam)
        ^
SyntaxError: invalid syntax
>>> inp=input('Europe floor?')
Europe floor?

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    inp=input('Europe floor?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> a=input("ievadi veselu skaitli: ")
ievadi veselu skaitli: 5
>>> type(a)
<type 'int'>
>>> a= raw input ("ievadi teksta rindu: ")
SyntaxError: invalid syntax
>>> a= raw_input ('ievadi teksta rindu: ')
ievadi teksta rindu: dsfhgsfdh
>>> type(a)
<type 'str'>
>>> 
