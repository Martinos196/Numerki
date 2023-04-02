import numpy as np

def Seidl(matrixA, matrixB,eps, ITERATION_LIMIT):
    A = np.array(matrixA)
    b = np.array(matrixB)

    # prints the system
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
        print(" + ".join(row), "=", b[i])
        print()

    x = np.zeros_like(b)
    if ITERATION_LIMIT==0:
        x_new = np.zeros_like(x)
        h = 0
        while True:
            for i in range(A.shape[0]):
                s1 = np.dot(A[i, :i], x_new[:i])
                s2 = np.dot(A[i, i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]
            h = h + 1
            if np.linalg.norm(x_new - x) < eps:
                print("Znaleziono rozwiązanie po "+ str(h) +" iteracjach")  
                print("Solution:")
                print(x)
                break  
            x=x_new.copy()     
    else:
        for j in range(ITERATION_LIMIT):
            x_new = np.zeros_like(x)
            for i in range(A.shape[0]):
                s1 = np.dot(A[i, :i], x_new[:i])
                s2 = np.dot(A[i, i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]
            if np.allclose(x, x_new, rtol=eps):
                break
            x = x_new
        print("Solution:")
        print(x)   

def is_gauss_seidel_convergent(matrixA):
    A = np.array(matrixA)
    n = len(A)
    # Sprawdzamy, czy macierz A jest silnie diagonalnie dominująca lub dodatnio określona
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) <= row_sum:
            return False
    return True