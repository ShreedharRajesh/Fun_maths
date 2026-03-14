import numpy as np
import matplotlib.pyplot as plt
import csv
import array
import random

def coinflips(ratio_tot,count_tot):
    count_tot=0

    for iter in range(1,100001):
        count=0
        H=0
        T=0
        for i in range(1,10001):
            Toss = [-1,1]
            CT = random.choice(Toss)
            if CT==1:
                H=H+1
                count = count + 1
                # print("H",end=" ")
            else:
                T=T+1
                count = count - 1
                # print("T",end=" ")

            if count == 1:
                ratio.append(H/(H+T))
                count_tot = count_tot + count
                # print("",ratio[iter-1])
                break
    # print(ratio)
    # print(count_tot)
    ratio_tot=0

    for j in range(1,len(ratio)):
        ratio_tot = ratio_tot + ratio[j]
    
    # print(ratio_tot)
    
    return ratio_tot,count_tot

if __name__ == "__main__":
    H=0
    T=0
    total=0
    ratio=[]
    count_tot=0
    ratio_tot=0
    ratio,count = coinflips(ratio_tot,count_tot)
    pi_val = 4*(ratio/count)
    print("pi = ",pi_val)