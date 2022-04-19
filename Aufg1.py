import math
import numpy as np
import matplotlib.pyplot as plt

Bier = 1.12
Abbauprozente = 0.5536
a = Bier
list = np.empty(10, dtype=float)
for i in range(10):
    a = a*(1-Abbauprozente)+Bier
    list[i] = a
    print('Promillegehalt: %s', a)

plt.plot(list)
plt.show()