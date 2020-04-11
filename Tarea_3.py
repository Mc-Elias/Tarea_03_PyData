#ELIAS MAMANI CALAMANI  C.I.: 9996275

import matplotlib.pyplot as plt
import numpy as np
import pylab as p

x=np.linspace(-10,10,100)

#Sigmoidal
def sigmoide(x):
    return 1/(1+np.exp(-x))

y=sigmoide(x)
plt.plot(x,y)
plt.grid()
plt.show()

#Tangencial
x1=p.linspace(-1.0,1.0,1000)
y1=(p.sin(2*p.pi*x1))/(p.cos(2*p.pi*x1))
t=10
y1[y1 > t] = np.nan
y1[y1 < -t] = np.nan
p.plot(x1,y1,"g-",lw=1)
plt.grid()
p.show()


#ReLu
def ReLu(x):
    return x*(x>0)

r=ReLu(x)
plt.plot(x,r)
plt.grid()
plt.show()