In [3]: stuff="Hello/nWorld!"

In [4]: stuff
Out[4]: 'Hello/nWorld!'

In [5]: print(stuff)
Hello/nWorld!

In [6]: stuff="X\nY"

In [7]: print(stuff)
X
Y

In [8]: len(stuff)
Out[8]: 3

In [9]: exit
user@epk428-19:~/RTR105$ nano teksts.txt
user@epk428-19:~/RTR105$ ls- l
No command 'ls-' found, did you mean:
 Command 'ls' from package 'coreutils' (main)
 Command 'lsh' from package 'lsh-client' (universe)
 Command 'lsx' from package 'suckless-tools' (universe)
 Command 'lsw' from package 'suckless-tools' (universe)
ls-: command not found
user@epk428-19:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: noraade_uz_failu=open('texts.txt', 'r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-1-3a91193ec3c4> in <module>()
----> 1 noraade_uz_failu=open('texts.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'texts.txt'

In [2]: noraade_uz_failu=open('tekts.txt', 'r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-2-ceb1a720efc1> in <module>()
----> 1 noraade_uz_failu=open('tekts.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'tekts.txt'

In [3]: noraade_uz_failu=open('text.txt', 'r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-3-0f4b97dbac16> in <module>()
----> 1 noraade_uz_failu=open('text.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'

In [4]: noraade_uz_failu=open('tksts.txt', 'r')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-4-87f96e963b7c> in <module>()
----> 1 noraade_uz_failu=open('tksts.txt', 'r')

FileNotFoundError: [Errno 2] No such file or directory: 'tksts.txt'

In [5]: noraade_uz_failu=open('teksts.txt', 'r')

In [6]: teksts.read()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-51ef68ae92e7> in <module>()
----> 1 teksts.read()

NameError: name 'teksts' is not defined

In [7]: teksts.txt.read()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-7ca54208133e> in <module>()
----> 1 teksts.txt.read()

NameError: name 'teksts' is not defined

In [8]: noraade_uz_failu=open('teksts.txt', 'r')

In [9]: fhand.read()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-0d53a74959bd> in <module>()
----> 1 fhand.read()

NameError: name 'fhand' is not defined

In [10]: noraade_uz_failu.read()
Out[10]: 'teksts\n'

In [11]: xfile=open('teksts.txt')

In [12]: for cheese in xfile:
    ...:     print(cheese)
    ...:     
teksts


In [13]: fhand=open("teksts.txt")

In [14]: count=0

In [15]: for line in fhand:
    ...:     count=count+1
    ...: count("Line Count: ", count)
    ...: 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-024c59df65a3> in <module>()
      1 for line in fhand:
      2     count=count+1
----> 3 count("Line Count: ", count)

TypeError: 'int' object is not callable

In [16]: for line in fhand:
    ...:     count=count+1
    ...: count("Line Count: ", count)
    ...: 
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-024c59df65a3> in <module>()
      1 for line in fhand:
      2     count=count+1
----> 3 count("Line Count: ", count)

TypeError: 'int' object is not callable

In [17]: fhand=open('teksts.txt')

In [18]: count=0

In [19]: for line in fhand:
    ...:     count=count+1
    ...: print('Line Count:',count)
    ...: 
Line Count: 1

In [20]: fhand=open('teksts.txt')

In [21]: inp=fhand.read()

In [22]: print(len(inp))
7

In [23]: print(inp[:20])
teksts


In [24]: fhand=open('teksts.txt')

In [25]: for line in fhand:
    ...:     if line.startswith('Form:'):
    ...:         print(line)
    ...:         

In [26]: fhand=open("teksts.txt")

In [27]: for line in fhand:
    ...:     line=line.rstrip()
    ...:     if not line.startswith("From:"):
    ...:         continue
    ...:     print(line)
    ...:     

In [28]: fhand=open("teksts.txt")

In [29]: for line in fhand:
    ...:     line=line.rstrip()
    ...:     if not "sdfg" in line:
    ...:         continue
    ...:     print(line)
    ...:     

In [30]: fname=input("enter the first name:  ")
enter the first name:  fsdh

In [31]: count=0

In [32]: for line in fhand:
    ...:     if line.startswith("subject: "):
    ...:         count=count+1
    ...: print("tur bija",count,"liiinijas", fname)
    ...: 
tur bija 0 liiinijas fsdh

