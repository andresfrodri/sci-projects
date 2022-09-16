import numpy as np
import matplotlib.pyplot as plt
n3=int(input('The final number so it\'ll be 1 - '))
count_list=range(1,n3+1)
l2=[i for i in count_list]
print('Your list is:',l2)
for i in l2:
  n=l2[i-1]
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
  plt.plot(array1,array2)
plt.xlabel('Steps')
plt.ylabel('Number')
plt.title(f'3x+1 for 1-{n3}')
plt.show()