#El reto ahora es superponer varias n
import numpy as np
import matplotlib.pyplot as plt

n=int(input('Put the number to see it\'s steps: '))
contador=1
listan1=[n]
listaC1=[contador]
while n != 1:
  if n%2!=0:
    n=3*n+1
    contador=contador+1
    listan1.append(n)
    listaC1.append(contador)
  else:
    n=n//2
    contador=contador+1
    listan1.append(n)
    listaC1.append(contador)
array1=np.array(listaC1)
array2=np.array(listan1)
plt.plot(array1,array2, label='line 1')
n1=int(input('Put another number to see it\'s steps: '))
contador2=1
listan2=[n1]
listaC2=[contador2]
while n1 != 1:
  if n1%2!=0:
    n1=3*n1+1
    contador2=contador2+1
    listan2.append(n1)
    listaC2.append(contador2)
  else:
    n1=n1//2
    contador2=contador2+1
    listan2.append(n1)
    listaC2.append(contador2)
array3=np.array(listaC2)
array4=np.array(listan2)
plt.plot(array3,array4, label='line 2')
plt.legend()
plt.xlabel('Steps')
plt.ylabel('Number')
plt.title(f'3x+1 for two')
plt.show()
