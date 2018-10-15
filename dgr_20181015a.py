user@epk428-19:~$ ls -l
total 36
drwxr-xr-x 2 user user 4096 Feb 10  2016 Desktop
drwxrwxr-x 3 user user 4096 Mar  5  2018 Documents
drwxr-xr-x 2 user user 4096 Mar  5  2018 Downloads
drwxr-xr-x 2 user user 4096 Mar  5  2018 Music
drwxr-xr-x 2 user user 4096 Mar  5  2018 Pictures
drwxr-xr-x 2 user user 4096 Mar  5  2018 Public
drwxr-xr-x 2 user user 4096 Mar  5  2018 Templates
drwxr-xr-x 2 user user 4096 Mar  5  2018 Videos
drwxrwxr-x 3 user user 4096 Feb  9  2016 VirtualBox VMs
user@epk428-19:~$ 
user@epk428-19:~$ git clone https://github.com/login/RTR105
Cloning into 'RTR105'...
Username for 'https://github.com': reinislacis
Password for 'https://reinislacis@github.com': 
remote: Repository not found.
fatal: repository 'https://github.com/login/RTR105/' not found
user@epk428-19:~$ git clone https://github.com/reinislacis/RTR105
Cloning into 'RTR105'...
remote: Enumerating objects: 33, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (27/27), done.
remote: Total 33 (delta 8), reused 17 (delta 3), pack-reused 0
Unpacking objects: 100% (33/33), done.
Checking connectivity... done.
user@epk428-19:~$ cd RTR105
user@epk428-19:~/RTR105$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x=5
>>> if x<10:
... print('mazaaks')
  File "<stdin>", line 2
    print('mazaaks')
        ^
IndentationError: expected an indented block
>>> x=5
>>> if x<10: print('mazaaks')
... if x>20: print('lielaaks')
  File "<stdin>", line 2
    if x>20: print('lielaaks')
     ^
SyntaxError: invalid syntax
>>> exit()
user@epk428-19:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: x=5

In [2]: if x<10:
   ...:     print('smaller')
   ...:     if x>20:
   ...:         print('bigger')
   ...:         print('finis')
   ...:         
smaller

In [3]: if x<10:
   ...:     print('smaller')
   ...: if x>20:
   ...:         print('bigger')
   ...: print('finis')
   ...: 
   ...:         
smaller
finis

In [4]: x=5

In [5]: if x==5:
   ...:     print('Equals5')
   ...: if x>4:
   ...:     print('Greater than 4')
   ...: if x>=5:
   ...:     print('Greater than of Equals 5')
   ...: if x<6: print('Less than 6')
   ...: if x<=5:
   ...:     print('Less than or Equals 5')
   ...: if x!=6:
   ...:     print('Not equal 6')
   ...:     
Equals5
Greater than 4
Greater than of Equals 5
Less than 6
Less than or Equals 5
Not equal 6

In [6]: x=5

In [7]: print('Before5')
Before5

In [8]: if x==5:
   ...:     print('Is 5)
  File "<ipython-input-8-87f6670814e6>", line 2
    print('Is 5)
                ^
SyntaxError: EOL while scanning string literal


In [9]: if x==5:
   ...:     print('Is 5')
   ...:     print('Is still 5')
   ...:     print('third5')
   ...: print('Aftervards5')
   ...: print('Before6')
   ...: ifx==6:
  File "<ipython-input-9-7725031db3e6>", line 7
    ifx==6:
           ^
SyntaxError: invalid syntax


In [10]: if x==5:
    ...:     print('Is 5')
    ...:     print('Is still 5')
    ...:     print('third5')
    ...: print('Aftervards5')
    ...: print('Before6')
    ...: if x==6:
    ...:     print('Is6')
    ...:     print('Is still 6')
    ...:     print('Third6')
    ...: print('Aftervards6')
    ...: 
Is 5
Is still 5
third5
Aftervards5
Before6
Aftervards6

In [11]: x=5

In [12]: ifx>2:
  File "<ipython-input-12-e04e1e8f39a9>", line 1
    ifx>2:
          ^
SyntaxError: invalid syntax


In [13]: x=5

In [14]: if x>2:
    ...:     print('Bigger than2')
    ...:     print('Still bigger')
    ...: print('Done with2')
    ...: 
Bigger than2
Still bigger
Done with2

In [15]: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than 2')
    ...:     print('Done with i',i)
    ...: print('All done')
    ...: 
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than 2
Done with i 3
4
Bigger than 2
Done with i 4
All done

In [16]: x=5

In [17]: if x>2:
    ...:     print('Bigger than2')
    ...:     print('Still bigger')
    ...: print('Done with2')
    ...: for i in range(5):
    ...:     print(i)
    ...:     if i>2:
    ...:         print('Bigger than2')
    ...:     print('Done with i',i)
    ...: print('All done')
    ...: 
Bigger than2
Still bigger
Done with2
0
Done with i 0
1
Done with i 1
2
Done with i 2
3
Bigger than2
Done with i 3
4
Bigger than2
Done with i 4
All done

In [18]: x=42

In [19]: if x>1:
    ...:     print('more than one')
    ...:     if x<100:
    ...:         print('Less than 100')
    ...: print('All done')
    ...: 
more than one
Less than 100
All done

In [20]: x=4

In [21]: if x>2:
    ...:     print('Bigger')
    ...: else:
    ...:     print('Smaller')
    ...: print('All done')
    ...: 
Bigger
All done

In [22]: x=4

In [23]: if x>2:
    ...:     print('Bigger')
    ...: else:
    ...:     print('Smaller')
    ...: print('All done')
    ...: 
Bigger
All done

In [24]: if x<2
  File "<ipython-input-24-67cb0dd8ad64>", line 1
    if x<2
          ^
SyntaxError: invalid syntax


In [25]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('medium')
    ...: else:
    ...:     print('large')
    ...: print('all done')
    ...: 
medium
all done

In [26]: x=0

In [27]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('medium')
    ...: else:
    ...:     print('large')
    ...: print('all done')
    ...: 
small
all done

In [28]: x=5

In [29]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('mediun')
    ...: else:
    ...:     print('large')
    ...: print('all done')
    ...: 
mediun
all done

In [30]: #no else

In [31]: x=5

In [32]: if x<2:
    ...:     print('small')
    ...: elif x<10:
    ...:     print('medium')
    ...: print('all done')
    ...: 
medium
all done

In [33]: if x<2:
    ...:     print('bellow 2')
    ...: elif x<20:
    ...:     print('bellow 20')
    ...: elif x<10:
    ...:     print('bellow 10')
    ...: else:
    ...:     print('something else')
    ...:     
bellow 20

In [34]: if x<88:
    ...:     print('bellow 2')
    ...: elif x<20:
    ...:     print('bellow 20')
    ...: elif x<10:
    ...:     print('bellow 10')
    ...: else:
    ...:     print('something else')
    ...:     
bellow 2

In [35]: if x<10:
    ...:     print('bellow 2')
    ...: elif x<20:
    ...:     print('bellow 20')
    ...: elif x<10:
    ...:     print('bellow 10')
    ...: else:
    ...:     print('something else')
    ...:     
bellow 2

In [36]: if x<11:
    ...:     print('bellow 2')
    ...: elif x<20:
    ...:     print('bellow 20')
    ...: elif x<10:
    ...:     print('bellow 10')
    ...: else:
    ...:     print('something else')
    ...:     
bellow 2

In [37]: astr='Hello Bob'

In [38]: try:
    ...:     istr=int(astr)
    ...: exept:
  File "<ipython-input-38-37d0e89e9e02>", line 3
    exept:
        ^
SyntaxError: invalid syntax


In [39]: try:
    ...:     istr=int(astr)
    ...: except:
    ...:     istr=-1
    ...: print('First', istr)
    ...: astr='123'
    ...: try:
    ...:     istr=int(astr)
    ...: except:
    ...:     istr=-1
    ...: print('second',istr)
    ...: 
First -1
second 123

In [40]: astr='Bob'

In [41]: try:
    ...:     print('hello')
    ...:     istr=int(astr)
    ...:     print('there')
    ...: except:
    ...:     istr=-1
    ...: print('all done')
    ...: 
hello
all done

In [42]: 

