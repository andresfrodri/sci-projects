import numpy as np
import matplotlib.pyplot as plt

n=int(input('Put the number to see it\'s steps: '))
initial=n
counter=0
listan1=[n]
listaC1=[counter]
while n != -10 and n != -2 and n !=-34 and n != -1:
  print(counter)
  if n%2!=0:
    if n<0:
      n=(3*n+1)*(-1)**(counter)
    else:
      n=(3*n+1)*(-1)**(counter-1)
    counter += 1
    listan1.append(n)
    listaC1.append(counter)
  else:
    if n<0:
      n=(n//2)*(-1)**(counter)
    else:
      n=(n//2)*(-1)**(counter-1)
    counter += 1
    listan1.append(n)
    listaC1.append(counter)
print(listan1)
array1=np.array(listaC1)
array2=np.array(listan1)
plt.plot(array1,array2)
plt.xlabel('Steps')
plt.ylabel('Number')
plt.title(f'3x+1 for {initial}')
plt.show()