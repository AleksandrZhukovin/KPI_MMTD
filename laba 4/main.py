import numpy as np


R1 = np.array([[1, 0.9, 0.8, 0.7, 1],
               [0.6, 1, 0.7, 0.3, 0.7],
               [0.3, 0, 0.2, 0.5, 0.1],
               [0.3, 0.5, 0.3, 1, 0.4],
               [0.3, 0.6, 0.5, 0.7, 1]])
l1 = 0.2

R2 = np.array([[1, 0, 1, 0, 0.6],
               [0.1, 1, 0.5, 0.4, 0.3],
               [0.5, 0.7, 1, 0, 0.7],
               [0.5, 0.3, 0, 1, 0.7],
               [0.7, 0.9, 0.8, 0.5, 1]])
l2 = 0.8

Q1 = np.minimum(R1*l1, R2*l2)

Q1_s = Q1.copy()
for i in range(Q1.shape[0]):
    for j in range(Q1.shape[1]):
        Q1_s[i, i] = 0
        if Q1_s[i, j] > Q1_s[j, i]:
            Q1_s[i, j] -= Q1_s[j, i]
            Q1_s[j, i] = 0
        else:
            Q1_s[j, i] -= Q1_s[i, j]
            Q1_s[i, j] = 0

non_dominate_alt = []
for i in range(Q1.shape[0]):
    xi = np.max(Q1_s[i, :])
    xj = np.max(Q1_s[:, i])
    non_dominate_alt.append(1 - round(max([xi, xj]), 2))

print(f'x{non_dominate_alt.index(max(non_dominate_alt))} - раціональний вибір. (індекси рахуються починаючи з 0)')
