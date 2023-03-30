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
        r = np.zeros_like(x)
        h = 0
        while True:
            x_new = np.zeros_like(x)
            for i in range(A.shape[0]):
                s1 = np.dot(A[i, :i], x_new[:i])
                s2 = np.dot(A[i, i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i, i]
                r[i] = b[i] - s1
            x=x_new   
            h = h + 1
            if h == 14:
                print("Podano za mały epsilon")
                break
            elif np.max(abs(r)) < eps:
                print("Znaleziono rozwiązanie po "+ str(h) +" iteracjach")  
                print("Solution:")
                print(x)
                break      
    else:
        for it_count in range(ITERATION_LIMIT):
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

def is_gauss_seidel_convergent(matrixA): #Funkcja sprawdzająca warunek zbieżności 
    A = np.array(matrixA)
    n = A.shape[0]
    for i in range(n):
        if A[i,i] <= 0:
            return False
    if not np.allclose(A, A.T):
        return False
    return True
