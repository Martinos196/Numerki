
import numpy as np

def gauss_seidel(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = x0.copy()

    for i in range(max_iterations):
        x_new = np.zeros(n)
        for j in range(n):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, j + 1:], x[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        if np.allclose(x, x_new, rtol=epsilon):
            return x_new
        x = x_new
    return x

A = np.array([[0.5, -0.0625, 0.1875, 0.0625],
              [-0.0625, 0.5, 0, 0],
              [0.1875, 0, 0.375, 0.125],
              [0.0625, 0, 0.125, 0.25]])
b = np.array([1.5,-1.625, 1, 0.4375])
x0 = np.zeros(4)
eps = 0.000000001
max_iter = 100

x = gauss_seidel(A, b, x0, eps, max_iter)
print(x)