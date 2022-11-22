import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def inter_graph(x, y,c):
    #La funcion recive 3 parametros: Dos vectores y el valor que se desea estimar 
    xi = np.array(x) 
    yi =  np.array(y)
    n = len(xi)
    a = np.zeros((n,n))
    for i in range(n):
        a.T[i] = xi**i
    a= np.linalg.solve(a,yi)
    xt=np.linspace(min(xi),max(xi),10000)
    yt=0
    for i in range(n):
        yt=yt+a[i]*xt**i
    d=0
    for i in range (len(a)):
        d=d+a[i]*c**(i)
    plt.plot(xi,yi,'ro')
    plt.plot(xt,yt,'b-')    
    plt.show()
    print('El valor estimado para {} es'.format(c),d)
    
def a (x):
  print(x*x)


def regre(x,y,c):
  x=np.array(x)
  y=np.array(y)
  for i in range (1,10,1):
    pol=np.polyfit(x,y,deg=i)
    pal = np.polyval(pol,x)
    sse = sum((y-pal)**2)
    tse = (len(y)-1)*np.var(y)
    r2 = 1-sse/tse
    if r2 >= 0.95:
      print('r2 =',r2)
      print('Grado:',i)
      xc=np.linspace(x.min(),x.max())
      yc=np.polyval(pol,xc)
      print('El valor estimado para x es',np.polyval(pol,c))
      plt.plot(x,y,'o',xc,yc,'-')
      plt.show()
      break
    if i ==9 and r2<0.95:
      print("--> Los datos no pueden ser representados mediante una regresion, Se recomienda usar el metodo de interpolacion <--") 
      inter_graph(x, y,c)
      break




"""
datos_valle = pd.read_csv("data\precios_valle.csv")
tomate = datos_valle['Tomate'] # precio_tomate
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
tomate = np.array(tomate)
meses = np.array(meses)
print (tomate,meses)
regre(meses,tomate,12.2)
"""
"""Para lo de los precios es mejor no ponerlos como parametro en una funcion objetivo, si no como una funcion adicional"""



