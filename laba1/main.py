import numpy as np

R = np.array([[1, 1, 1, 1, 0],
              [1, 1, 0, 0, 1],
              [1, 0, 1, 1, 1],
              [1, 0, 1, 1, 1],
              [0, 1, 0, 0, 0]])

# рефлексивність
ref = True
if list(np.diagonal(R)).count(0) == len(np.diagonal(R)):
    print('Aнтирефлексивне')
elif 0 in np.diagonal(R):
    print("Нерефлексивне")
    ref = False
else:
    print("Рефлексивне")


# симетричність
not_in_relation = 0
for i in range(5):
    for j in range(5):
        if R[i, j] != R[j, i]:
            not_in_relation += 1
if not_in_relation == 0:
    print('Симетричне')
elif not_in_relation == 20 and ref == True:
    print("Антисиметричне")
elif not_in_relation == 20:
    print('Асиметричне')
else:
    print("Несеметричне")


# транзитивність
R_sqr = np.dot(R, R)
tr = True
for i in range(5):
    for j in range(5):
        if R[i, j] == 0 and R_sqr[i, j] == 1:
            tr = not tr
            break
if tr:
    print("Транзитивне")
else:
    print("Нетранзитивне")

# max, min, inf, sup
for i in range(5):
    if 0 not in R[i, :]:
        print(f'x{i} - найкращій')
    if 1 not in R[i, :]:
        print(f'x{i} - гірший')

R_str = np.copy(R)
for i in range(5):
    R_str[i, i] = 0
    for j in range(5):
        if R_str[i, j] == 1 and R_str[j, i] == 1:
            R_str[i, j], R_str[j, i] = 0, 0

print("Строге відношення:", R_str, sep='\n')

for i in range(5):
    if 1 not in R_str[i, :]:
        print(f'x{i} - мінімальний')
    if 1 not in R_str[:, i]:
        print(f"x{i} - максимальний")

# оберенене, доповнене
R_dop = np.zeros((5, 5))
for i in range(5):
    for j in range(5):
        if R[i, j] == 0:
            R_dop[i, j] = 1
R_obr = R.T

print('Доповнення:', R_dop, "Оберенене відношення: ", R_obr, sep='\n')

