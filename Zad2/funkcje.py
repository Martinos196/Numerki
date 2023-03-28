import numpy as np

def Seidl(eps,ITERATION_LIMIT):
    A = np.array([[0.5, -0.0625, 0.1875, 0.0625],
              [-0.0625, 0.5, 0, 0],
              [0.1875, 0, 0.375, 0.125],
              [0.0625, 0, 0.125, 0.25]])
    b = np.array([1.5,-1.625, 1, 0.4375])

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
            print("Current solution:", x)
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
            elif abs(np.max(r)) < eps:
                print("Znaleziono rozwiązanie po "+ str(h) +" iteracjach")  
                break      
    else:
        for it_count in range(ITERATION_LIMIT):
            print("Current solution:", x)
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

