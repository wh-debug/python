import numpy as np

def native_matrix_and_vector(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]
    return x
    
num1 = np.array([[1,2,3,4],
                [3,4,5,6],
                [5,6,7,8]])

num2 = np.array([1,2,3,4])

print(num2.shape[0])