#print (vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import cos, sqrt, linspace
#print (vars())

def f(x):
    return cos(sqrt(x))


x=linspace(-5,7,20)
#print (vars())

y=cos(sqrt(x))

legend = []
#print (legend)

from matplotlib import pyplot as plt
#print()plt._doc_)
plt.axis([-1, 9, -4, 2])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("funkcija $cos(sqrt(x))$ un taas atvasinaajumu")
plt.plot(x,y,"k")
legend.append("$cos(sqrt(x))$ - dafault- viss ir savienotis ar taisaam liinijaam")
#print(legend)
plt.plot(x,y, "ro")
legend.append("$cos(sqrt(x))$ - tikai dazhi punkti")
#print(legend)

N= len(x)
deltax = x[1] - x[0]
derivative = []

for i in range(N):
    temp=(f(x[i] + deltax)-f(x[i])) / deltax
    derivative.append(temp)

plt.plot(x,derivative,"y")
legend.append("$cos(sqrt(x))$ atvasinaajums - viss ir savienots ar taisnaam liinijaam")
plt.plot(x,derivative,"go")
legend.append("$cos(sqrt(x))$ atvasinaajums - dazhi punkti")


derivative_through_array = []

for i in range (N-1):
    temp = (y[i+1]- y[i]) / (x[i+1]- x[i])
    derivative_through_array.append(temp)

    
plt.plot(x[0:N-1], derivative_through_array,"m")
legend.append("$cos(sqrt(x))$ atvasiinaajums, izmatojot masiiva vertibas")
plt.plot(x[0:N-1], derivative_through_array,"bo")
legend.append("$cos(sqrt(x))$ atvasiinaajums, izmatojot masiiva vertibas")
    
plt.plot(3.354, -0.279, "ch", markersize = 10)

#print(plt.legend._doc_)
#plt.legend(legend, loc="lower left")
plt.legend(legend, loc= 3, fancybox=True, framealpha=0.5, )
plt.show()
