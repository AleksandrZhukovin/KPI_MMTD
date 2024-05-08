"""
f(x1, x2) = 2*x1 + 5*x2 -> max
2*x1 + 3*x2 >=~ 6     <- condition_1
x1 + 6*x2 <=~ 18      <- condition_2
2*x1 + 3*x2 <=~ 12    <- condition_3
x1, x2 >= 0

         |0,    2*x1 + 3*x2 <= 4 || 2*x1 + 3*x2 >= 14 || x1 + 6*x2 >= 20
miu(x) = |0.5,   4 <= 2*x1 + 3*x2 <= 5 || 13 <= 2*x1 + 3*x2 <= 14 || 19 <= x1 + 6*x2 <= 20
         |0.7,   5 <= 2*x1 + 3*x2 <= 6 || 12 <= 2*x1 + 3*x2 <= 13 || 18 <= x1 + 6*x2 <= 19
         |1,     2*x1 + 3*x2 >= 6 && 2*x1 + 3*x2 <= 12 && x1 + 6*x2 <= 18
"""
import numpy as np


# Lambda1 = 0.5
coefs_a = np.array([[2, 3], [1, 6]])
coefs_b = np.array([14, 20])
res = np.linalg.solve(coefs_a, coefs_b)
x1_1, x2_1 = res[0], res[1]

# Lambda2 = 0.7
coefs_a = np.array([[2, 3], [1, 6]])
coefs_b = np.array([13, 19])
res = np.linalg.solve(coefs_a, coefs_b)
x1_2, x2_2 = res[0], res[1]

# Lambda3 = 1
coefs_a = np.array([[2, 3], [1, 6]])
coefs_b = np.array([12, 18])
res = np.linalg.solve(coefs_a, coefs_b)
x1_3, x2_3 = res[0], res[1]

print('-'*29)
print(f'|{"x1":^6}|{"x2":^6}|{"f":^6}|{"mue":^6}|')
print('-'*29)
print(f'|{x1_3:^6.2f}|{x2_3:^6.2f}|{2*x1_3+5*x2_3:^6.2f}|{"1":^6}|')
print('-'*29)
print(f'|{x1_2:^6.2f}|{x2_2:^6.2f}|{2*x1_2+5*x2_2:^6.2f}|{"0.7":^6}|')
print('-'*29)
print(f'|{x1_1:^6.2f}|{x2_1:^6.2f}|{2*x1_1+5*x2_1:^6.2f}|{"0.5":^6}|')
print('-'*29)


