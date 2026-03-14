import numpy as np
import matplotlib.pyplot as plt
import csv
import array

def get_rref (mat,rows,cols):

    m = 0
    s = 0

    for i in range(1,rows):
        # print ("i = ", i)
        for j in range (0, cols):
            # print("j = ",j)
            if mat[i][j] == 0: #ignores the zeros. Will help in efficiency
                continue
            if mat[i][j] == 1: #Finds the first element in the row with 1. Then only runs this iteration
                for k in range (0,i):
                    pivot = mat[k][j]
                    for l in range(0,cols):
                        mat[k][l] = mat[k][l] - (pivot*mat[i][l])
                        m = m + 1
                        s = s + 1
                        # print ("k = ",k)
                        # print ("l = ",l)
                        # print (mat)
                    m = m - j
                    s = s - j
                break
    
    rref_mat = mat

    return rref_mat,m,s

if __name__ == "__main__":

    mat = [[1,5,8,4,7,8],[0,1,3,1,8,9],[0,0,1,7,1,3],[0,0,0,0,0,1]]
    print (mat)
    rows = len(mat)
    print (rows)
    cols = len(mat[0])
    print (cols)
    rref_mat, mults, subts = get_rref(mat,rows,cols)
    print(rref_mat)
    print (mults)
    print (subts)
