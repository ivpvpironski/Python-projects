import numpy as np
import matplotlib.pyplot as plt
import math

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

d = b*b - 4*a*c
print(d)

if d == 0:
    x = -b/(2*a)
    print('x= ', x)
elif d > 0:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print('x1= '+str(x1), 'x2= '+str(x2), sep='\n')
else:
    xr = -b/(2*a)
    xi = math.sqrt(math.fabs(d))
    print('x1= ' + str(xr)+'-i'+str(xi),
          'x2= '+str(xr)+'+i'+str(xi), sep='\n')

xplt = np.arange(-20, 20, 1)
yplt = a*xplt*xplt+b*xplt+c

plt.plot(xplt, yplt, color='indigo', label = 'y = a*x^2 + b*x + c')
yplt = xplt**2
plt.plot(xplt, yplt, color='yellowgreen', label = 'y = x^2')
plt.legend()
plt.show()