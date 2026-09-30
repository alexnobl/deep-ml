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
    """a
    t_matrix = np.zeros(a.shape[1], a.shape[0])
    return t_matrix"""
    t_matrix = []
    for column in zip(*a):
        t_matrix.append(list(column))
    return t_matrix