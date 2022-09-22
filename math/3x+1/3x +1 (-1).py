import numpy as np
import matplotlib.pyplot as plt
"""This is an idea to see what happens with the 3x+1 if each step the number becomes 
negative and then positive... Let's see how much the patterns changes
"""


n=int(input('Set the initial number: '))
initial = n
contador=0
listan1=[n]
listaC1=[contador]
while n != -10 and n != -2 and n !=-34 and n != -1:
  if n%2!=0:
    if n<0:
      n=(3*n+1)*(-1)**(contador)
    else:
      n=(3*n+1)*(-1)**(contador-1)
    contador=contador+1
    listan1.append(n)
    listaC1.append(contador)
  else:
    if n<0:
      n=(n//2)*(-1)**(contador)
    else:
      n=(n//2)*(-1)**(contador-1)
    contador=contador+1
    listan1.append(n)
    listaC1.append(contador)
array1=np.array(listaC1)
array2=np.array(listan1)
plt.plot(array1,array2)
plt.xlabel('Steps')
plt.ylabel('Number')
plt.title(f'3x+1 for {initial}')
plt.show()