import numpy as np
import matplotlib.pyplot as plt
import csv
import array
import random

def gcd(x,y):

    x_fac = []
    y_fac = []

    for u in range(2,x+1):
        if x%u == 0:
            x_fac.append(u)

    for v in range(2,y+1):
        if y%v == 0:
            y_fac.append(v)

    # print(x_fac)
    # print(y_fac)

    counter = 0

    for c in range (0,len(x_fac)):
        for d in range (0,len(y_fac)):
            if x_fac[c] == y_fac[d]:
                counter = counter + 1
                break
    # print(counter)


    return counter

def zeta_func(x):

    a = [0]*(x)
    cop=0
    nocop=0
    
    for i in range (1,10001):
        count=0
        for j in range (0,x):
            a[j] = random.randint(1,10001)
        a_sort = np.sort(a)
        # print(a_sort)

        for k in range (0,x):
            for l in range (1,x-k):
                hcf = gcd(a_sort[k],a_sort[k+l])
                if hcf != 0:
                    count = count + 1
                # print(a_sort[k+l]%a_sort[k])
                # if a_sort[k+l]%a_sort[k] == 0:
                #     count = count + 1

        # print(count)

        if count == 0:
            cop=cop+1
        else:
            nocop = nocop+1            
    
    print("not coprime=",nocop)
    print("coprime=",cop)


    return cop,nocop

if __name__ == "__main__":
    x=2
    cop,nocop=zeta_func(x)
    zeta_val=(cop+nocop)/cop
    print("zeta(2) = ",zeta_val)
    