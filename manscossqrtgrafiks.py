import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
from numpy import linspace, cos, sqrt
x= linspace(0, 20, 200)
y= cos(sqrt(x))

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(sqrt(x))$')
plt.plot(x, y)
plt.plot(x, y, color = "#FF0000")

plt.show()
