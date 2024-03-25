import numpy as np

coal_amount = (400, 250, 350, 100)  # кількість кожного виду вугілля
"""Пропорції та ціна"""
A = (1, 1, 1, 1, 120)
B = (3, 1, 2, 1, 100)
C = (2, 2, 1, 3, 150)

"""Коефіцієнти функцій"""
f1_coef = np.array([[1, 1, 1, 1, 3, 1, 2, 1, 2, 2, 1, 3]])
f2_coef = np.array([[120, 120, 120, 120, 300, 100, 200, 100, 300, 300, 150, 450]])

f1_max = 1000
f1_min = 0

f1_norm_coef = f1_coef / (f1_max - f1_min)

f2_max = 300000
f2_min = 0

f2_norm_coef = f2_coef / (f2_max - f2_min)
# print(f2_norm_coef)

alph_f1 = 0.4
alph_f2 = 0.6

F_coef = f1_norm_coef * alph_f1 + f2_norm_coef * alph_f2

print(F_coef)

# cost 120 000, amount 800
