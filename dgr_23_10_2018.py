ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: n=5

In [2]: while n>0:
   ...:     print(n)
   ...:     n=n-1
   ...: print('blastoff')
   ...: print(n)
   ...: 
5
4
3
2
1
blastoff
0

In [3]: while True:
   ...:     line=input('>')
   ...:     if line=='done':
   ...:         break
   ...:     print(line)
   ...: print('done')
   ...: 
>

>done
done

In [4]: while True:
   ...:     line=input('>')
   ...:     if line[0]=='#':
   ...:         contiune
   ...:     if line=='done':
   ...:         break
   ...:     print(line)
   ...: print(Done!)
  File "<ipython-input-4-0e0fb4e58a1f>", line 8
    print(Done!)
              ^
SyntaxError: invalid syntax


In [5]: while True:
   ...:     line=input('>')
   ...:     if line[0]=='#':
   ...:         contiune
   ...:     if line=='done':
   ...:         break
   ...:     print(line)
   ...: print('Done!')
   ...: 
>hello
hello
>asaaha
asaaha
>done
Done!

In [6]: for i in [5,4,3,2,1]:
   ...:     print(i)
   ...: print('blastoff')
   ...: 
5
4
3
2
1
blastoff

In [7]: friends=['pīrādziņš','Cūciņa','Reiks']

In [8]: for friend in friends:
   ...:     print('apsveicu',friend)
   ...: frint('done')
   ...: 
apsveicu pīrādziņš
apsveicu Cūciņa
apsveicu Reiks
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-a9809127445c> in <module>()
      1 for friend in friends:
      2     print('apsveicu',friend)
----> 3 frint('done')

NameError: name 'frint' is not defined

In [9]: for friend in friends:
   ...:     print('apsveicu',friend)
   ...: print('done')
   ...: 
   ...: 
apsveicu pīrādziņš
apsveicu Cūciņa
apsveicu Reiks
done

In [10]: print('before')
before

In [11]: print('Before')
Before

In [12]: for thing in [9,41,12,3,74,15]:
    ...:     print(thing)
    ...: print('after')
    ...: 
9
41
12
3
74
15
after

In [13]: largest_so_far=-1

In [14]: print('Before',largest_so_far)
Before -1

In [15]: zork=0

In [16]: print('before', zork)
before 0

In [17]: for thing in [9,41,12,3,74,15]:
    ...:     zork=zork+1
    ...:     print(zork, thing)
    ...: print('After', zork)
    ...: 
1 9
2 41
3 12
4 3
5 74
6 15
After 6

In [18]: count=0

In [19]: sum=0

In [20]: print('before', count, sum)
before 0 0

In [21]: for value in [9,41,12,3,74,15]:
    ...:     count=count+1
    ...:     sum=sum+value
    ...:     print(count,sum,value)
    ...: print('after', count,sum,sum/count)
    ...: 
1 9 9
2 50 41
3 62 12
4 65 3
5 139 74
6 154 15
after 6 154 25.666666666666668

In [22]: print('before')
before

In [23]: for value in [9,41,12,3,74,15]:
    ...:     if value>20:
    ...:         print('large number', value)
    ...: print('after')
    ...: 
large number 41
large number 74
after

In [24]: smallest=None

In [25]: print('Before')
Before

In [26]: for value in [9,41,12,3,74,15]:
    ...:     if smallest is None:
    ...:         smallest=value
    ...:     elif value<smallest:
    ...:         smallest=value
    ...:     print(smallest,value)
    ...: print('After',smallest)
    ...: 
9 9
9 41
9 12
3 3
3 74
3 15
After 3

In [27]:
