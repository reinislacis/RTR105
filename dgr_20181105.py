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
user@epk428-19:~$ git
git                 git-shell           git-upload-pack
git-receive-pack    git-upload-archive  
user@epk428-19:~$ 
user@epk428-19:~$ git 
add                  format-patch         remote 
am                   fsck                 repack 
annotate             gc                   replace 
apply                get-tar-commit-id    request-pull 
archive              grep                 reset 
bisect               help                 revert 
blame                imap-send            rm 
branch               init                 shortlog 
bundle               instaweb             show 
checkout             interpret-trailers   show-branch 
cherry               log                  stage 
cherry-pick          merge                stash 
clean                mergetool            status 
clone                mv                   submodule 
commit               name-rev             subtree 
config               notes                tag 
describe             pull                 verify-commit 
diff                 push                 whatchanged 
difftool             rebase               worktree 
fetch                reflog               
filter-branch        relink               
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
user@epk428-19:~$ git clone https://github.com/reinislacis/RTR105
Cloning into 'RTR105'...
remote: Enumerating objects: 44, done.
remote: Counting objects: 100% (44/44), done.
remote: Compressing objects: 100% (38/38), done.
remote: Total 44 (delta 11), reused 25 (delta 3), pack-reused 0
Unpacking objects: 100% (44/44), done.
Checking connectivity... done.
user@epk428-19:~$ cd RTR106
bash: cd: RTR106: No such file or directory
user@epk428-19:~$ cd RTR105
user@epk428-19:~/RTR105$ ipython
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: str1='sveiks'

In [2]: str2='Artur'

In [3]: bob=str1+str2

In [4]: print(bob)
sveiksArtur

In [5]: name=input('Enter:')
Enter:Reinis

In [6]: print(name)
Reinis

In [7]: apple=input('Enter:')
Enter:100

In [8]: x=int(apple)-10

In [9]: print(x)
90

In [10]: fruit='banana'

In [11]: letter=fruit[1]

In [12]: print(letter)
a

In [13]: x=3

In [14]: w=fruit[x-1]

In [15]: print(w)
n

In [16]: fruit='banana'

In [17]: print(len)fruit))
  File "<ipython-input-17-1bb313561dfd>", line 1
    print(len)fruit))
                  ^
SyntaxError: invalid syntax


In [18]: fruit='banana'

In [19]: print(len(fruit))
6

In [20]: fruit='banana'

In [21]: index=0

In [22]: while index<len(fruit):
    ...:     letter=fruit[index]
    ...:     print(index, letter)
    ...:     index=index+1
    ...:     
0 b
1 a
2 n
3 a
4 n
5 a

In [23]: fruit='ananaas'

In [24]: for letter in fruit:
    ...:     print(letter)
    ...:     
a
n
a
n
a
a
s

In [25]: index=0

In [26]: while index<len(fruit):
    ...:     letter=fruit[index]
    ...:     print(letter)
    ...:     index=index+1
    ...:     
a
n
a
n
a
a
s

In [27]: word='banana'

In [28]: count=0

In [29]: for letter in word:
    ...:     if letter=='a':
    ...:         count=count+1
    ...: print(count)
    ...: 
3

In [30]: s='Man garsho ananaas'

In [31]: print(s[0:8])
Man gars

In [32]: fruit='ananaas'

In [33]: 'n' in fruit
Out[33]: True

In [34]: 'm' in fruit
Out[34]: False

In [35]: if 'a''in fruit:
  File "<ipython-input-35-1002db435b34>", line 1
    if 'a''in fruit:
                    ^
SyntaxError: EOL while scanning string literal


In [36]: if word =='banana':
    ...:     print('All right, bananas.')
    ...: if word<'banana':
    ...:     print('Your word,'+word+', comes before babana.')
    ...: elif word>'banana':
    ...:     print('Your word,'+word+'comes after banana.')
    ...: else:
    ...:     print('All right, bananas.')
    ...:     
All right, bananas.
All right, bananas.

In [37]: greet='Hello Banana'

In [38]: zap=greet.lower()

In [39]: print(zap)
hello banana

In [40]: print(greet)
Hello Banana

In [41]: stuff='Hello word'

In [42]: type(stuff)
Out[42]: str

In [43]: dir(stuff)
Out[43]: 
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count',
 'encode',
 'endswith',
 'expandtabs',
 'find',
 'format',
 'format_map',
 'index',
 'isalnum',
 'isalpha',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',
 'lower',
 'lstrip',
 'maketrans',
 'partition',
 'replace',
 'rfind',
 'rindex',
 'rjust',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']

In [44]: fruit='ananaas'

In [45]: pos=fruit.find('ass')

In [46]: print(pos)
-1

In [47]: greet='Hello Bob'

In [48]: nnn=greet.upper()

In [49]: print(nnn)
HELLO BOB

In [50]: www=greet.lower()

In [51]: print(www)
hello bob

In [52]: greet='Hello Bob'

In [53]: nstr=greet.replace('Bob','Jane')

In [54]: print(nstr)
Hello Jane

In [55]: greet='   Hello Bob'

In [56]: greet.lstrip()
Out[56]: 'Hello Bob'

In [57]: line='Please have a nice day'

In [58]: line.startswith('Please')
Out[58]: True

In [59]: line.startswith('P')
Out[59]: True

In [60]: line.startswith('p')
Out[60]: False

