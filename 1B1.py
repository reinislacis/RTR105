import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import cos, linspace, sin
x=linspace(0, 7, 70)
y=cos(x)

from matplotlib import pyplot as plt

plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y)
plt.plot(x, y, color = "#530000")

y2=sin(x)


plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$cos(x)$')
plt.plot(x, y2)
plt.plot(x, y2, color = "#530000")



plt.show()

