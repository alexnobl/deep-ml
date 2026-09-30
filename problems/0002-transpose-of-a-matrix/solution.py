import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # solution with python
    t_matrix = []
    for column in zip(*a):
        t_matrix.append(list(column))
    return t_matrix
    
    '''
    # solution 2
    a = np.asarray(a)
    t_matrix = np.zeros((a.shape[1], a.shape[0]))
    for i in range(len(a)):
        for j in range(len(a[i])):
            t_matrix[j][i] = a[i][j]
    return t_matrix

    #or
    return np.transpose(a) 
    
    '''