# Program to multiply two matrices using nested loops

N = 250

import numpy as np


def create_matrix1(N):
    X = np.random.randint(0,100, size=(N,N))
    return(X)



def create_matrix2(N):
    Y = np.random.randint(0,100, size=(N,N+1))
    return(Y)

def multiply_matrix(X,Y):
    result = np.matmul(X,Y)
    return(result)

X = create_matrix1(N)
Y = create_matrix2(N)
result = multiply_matrix(X,Y)
print(result)