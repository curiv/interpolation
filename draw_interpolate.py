#!/usr/bin/env python3
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

def draw_lagranz(x,y,t):
    z=0
    for j in range(len(y)):
     p1=1; p2=1
     for i in range(len(x)):
         if i==j:
             p1=p1*1; p2=p2*1
         else:
             p1=p1*(t-x[i])
             p2=p2*(x[j]-x[i])
     z=z+y[j]*p1/p2
    return z

def draw_spline(value_x,x_knots,y_knots):
    tck = interpolate.splrep(x_knots, y_knots)
    return interpolate.splev(value_x, tck)

'''
Изменяем точки здесь!
'''
x_knots = [-4,-3,-2,-1,0,1,2,3,4]
y_knots = [0,0,0,1,2,-1,0,0,0]

x=np.array(x_knots, dtype=float)
y=np.array(y_knots, dtype=float)

'''
Вычисляем значения полинома Лагранджа и кубического сплайна!
'''
xnew_poly=np.linspace(np.min(x),np.max(x),100)
ynew_poly=[draw_lagranz(x,y,i) for i in xnew_poly]
#===========================================================
xnew_spline=np.linspace(np.min(x),np.max(x),100)
ynew_spline=[draw_spline(x,x_knots,y_knots) for x in xnew_spline]

'''
Рисуем оси координат!
'''

plt.axhline(y=0)
plt.axvline(x=0)
plt.axis('auto')

'''
Рисуем графики!
'''
plt.plot(x,y,'o',xnew_poly,ynew_poly,color = 'black',label='полином Лагранджа')
plt.plot(x,y,'o',xnew_spline,ynew_spline,color = 'red',label='кубический сплайн')

'''
Задаём параметры графика
'''
plt.grid(True,which='both')
plt.xlabel('x',fontsize='xx-large')
plt.ylabel('f(x)',fontsize='xx-large')
plt.title('Интерполирование',fontsize='xx-large')
plt.legend()
plt.show()
