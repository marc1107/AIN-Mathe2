import matplotlib.pyplot as plt
import numpy as np


def functionA(x):
    value = []
    # für jeden Wert in x
    for i in range(len(x)):
        # Prüfen ob durch 0 geteilt wird
        if x[i] != 1:
            value.append(1 / (1 - x[i]))
        else:
            value.append("division by 0")
    return value


def functionB(n, x):
    value = []
    # für jeden Wert in x
    for i in range(len(x)):
        # mit 0 initialisieren
        value.append(0)
        # von 0 bis n (in Python n+1, weil sonst nur bis n-1 addiert wird)
        for j in range(0, n + 1):
            value[i] = value[i] + x[i] ** j
    return value


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\na)", functionA(array))
print("\nb)", functionB(10, array))

# x ist -1 bis 0,9
# y ist
intervallVon = -1
intervallBis = 0.9
intervallGes = intervallBis - intervallVon
intervall = []
stuetzstellen = 100
schrittgroesse = intervallGes / stuetzstellen

# damit -1 auch noch drin ist
temp = intervallVon - schrittgroesse

for i in range(stuetzstellen):
    temp = temp + schrittgroesse
    intervall.append(temp)

plt.plot(intervall, functionA(intervall))
plt.plot(intervall, functionB(4, intervall))
plt.legend(['f', 'geom'])
plt.show()
