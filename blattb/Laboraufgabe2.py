import math

import matplotlib.pyplot as plt
import numpy as np

a = 2 * 10 ** (-2)
y = 2100
b = 2 * y ** (-2)
e = math.e


def functionB(t):
    # return a * math.exp((-b) * (t - y) ** 2)
    return a * e ** ((-b) * (t - y) ** 2)


# anwesende Personen B(T) berechnen
t = []
bStrich = []
# Array für ganzzahlige Personen
B = []
# Array für nicht ganzzahlige Personen zur genauen Berechnung bei den Zeitpunkten
BTemp = []
for i in range(0, 4201):
    t.append(i)
    bStrich.append(functionB(i))
    if len(B) > 0:
        BTemp.append(BTemp[i - 1] + bStrich[i])
        B.append(round(BTemp[i]))
    else:
        BTemp.append(bStrich[i])
        B.append(round(BTemp[i]))


# Ankunftszeiten T(B) berechnen
# To-Do: Formeln zur Berechnung finden?


# Kassen je Besucher: K(B) berechnen
K = []
for i in range(len(B)):
    if B[i] != 0:
        K.append(math.log(B[i]) + 0.5)
        # K.append(math.log(BLocal, 10) + 0.5)
    else:
        K.append(0)


# Kassenöffnung nach Zeit berechnen
# To-Do: Formel zur Berechnung finden



fig, ax = plt.subplots(2, 2)
# Plot für anwesende Personen B(T)
ax[0, 0].plot(t, B)
ax[0, 0].set_xlabel("Zeit T")
ax[0, 0].set_ylabel("Personen B")
ax[0, 0].set_title("anwesende Personen B(T)")

# Plot für Ankunftszeiten T(B)
ax[0, 1].plot(B, t)
ax[0, 1].set_xlabel("Personen B")
ax[0, 1].set_ylabel("Zeit T(B)")
ax[0, 1].set_title("Ankunftszeiten T(B)")

# Plot für Kassen je Besucher: K(B)
# To-Do: In Punkten darstellen
ax[1, 0].plot(B, K)
ax[1, 0].set_xlabel("Personen B")
ax[1, 0].set_ylabel("Kassen K(B)")
ax[1, 0].set_title("Kassen je Besucher: K(B)")

# Plot für Kassenöffnung nach Zeit
# To-Do: In Punkten darstellen
ax[1, 1].plot(t, K)
ax[1, 1].set_xlabel("Zeit T(B)")
ax[1, 1].set_ylabel("Kassenöffnungen")
ax[1, 1].set_title("Kassenöffnung nach Zeit")

plt.show()

print(bStrich)
