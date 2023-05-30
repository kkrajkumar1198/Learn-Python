#Given a square binary matrix 'mat [n][n]', find 'K' such that all elements in the Kth row are '0' and all elements in the Kth column are '1' The value of mat[k][k] can be anything (either 'O' or '1'). If no such k exists, return - 1

from os import *
from sys import *
from collections import *
from math import *

def findRowK(mat):
    # n as number of rows
    n = len(mat)
    # not valid then return -1
    potential_K = -1
    
    # m[k,k] can be 0 or 1, add the condition in the row 
    for k in range(n):
        row_zero = True
        column_one = True

        for i in range(n):
            if i != k and mat[k][i] != 0:
                row_zero = False
                break

        for i in range(n):
            if mat[i][k] != 1:
                column_one = False
                break

        if row_zero or column_one:
            potential_K = k
            break

    if potential_K >= 0:
        return potential_K
    else:
        return -1
        
