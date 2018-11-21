import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace
x = linspace(0, 4, 101)
y = sin(x)

from numpy import sin, linspace
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$ un tās izvitzījums rindā')
plt.plot(x, y2)
plt.plot(x, y2, color = "#530000")

y1=x
plt.plot(x, y1, color = "#530000")

y2 = y1 - x*x*x/(1*2*3)
plt.plot(x, y2, color = "#530000")

plt.show()






