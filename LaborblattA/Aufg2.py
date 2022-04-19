import math
import matplotlib.pyplot as plt
import numpy as np

list = [0.1,0.3,0.9,1.,1.5]

x = 0.5
l = 0.5

print("Aufgabe 2 i:")
for a in range(100):
    x = l * x * (1 - x)
print(x)


print("\nAufgabe 2 ii:")
for li in list:
    x = 0.5
    for a in range(100):
        x = li * x * (1 - x)
    print(x)


print("\nAufgabe 2 iii:")
list2 = np.empty(100, dtype=float)
for j in range(1, 101):
    list2[j-1] = (j-1)*2/99

for li in list2:
    x = 0.5
    for a in range(100):
        x = li * x * (1 - x)
print(x)


print("\nAufgabe 2 iv:")
for j in range(1, 101):
    list2[j-1] = (j-1)*4/99

for li in list2:
    x = 0.5
    for a in range(100):
        x = li * x * (1 - x)
print(x)


print("\nAufgabe 2 v [0-2] last 4:")
for j in range(1, 101):
    list2[j-1] = (j-1)*2/99

for li in list2:
    x = 0.5
    for a in range(100):
        x = li * x * (1 - x)
        if a >= 96:
            print(x)


print("\nAufgabe 2 v [0-4] last 4:")
for j in range(1, 101):
    list2[j-1] = (j-1)*4/99

for li in list2:
    x = 0.5
    for a in range(100):
        x = li * x * (1 - x)
        if a >= 96:
            print(x)


print("\nAufgabe2 vi a):")