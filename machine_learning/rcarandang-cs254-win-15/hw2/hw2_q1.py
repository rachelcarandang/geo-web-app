import math
import numpy as np
import scipy.linalg as sl
import matplotlib.pyplot as plt



def get_laplacian():
    data_list = np.loadtxt('hw2-data/usps-ascii.txt', delimiter=',')

    vector_list = []
    for row in range(len(data_list)):
        vector_list.append(data_list[row][1:])

    # create matrix
    n=len(data_list)
    laplacian = np.zeros((n,n))
    sigma = 1
    for i in range(n):
        for j in range(n):
            if i!=j:
                laplacian[i][j] = -exponential_distance(vector_list[i], vector_list[j], sigma)
            if i==j:
                summation = 0
                for k in range(n):
                    if k!=i:
                        summation += exponential_distance(vector_list[i], vector_list[k], sigma)
                laplacian[i][j]= summation

    evals, evecs = sl.eigh(laplacian, eigvals=(1,2))
    e0 = [row[0] for row in evecs]
    e1 = [row[1] for row in evecs]
        
    digit_list = []
    for row in range(len(data_list)):
        digit_list.append(data_list[row][0])  
    cmap = plt.get_cmap('rainbow')(digit_list)
    
    plt.scatter(e0, e1, color=cmap, lw=0)
    plt.show()


def exponential_distance(x, y, sigma):
    norm = np.linalg.norm(x - y)
    return math.exp(-norm**2/(2*sigma**2))

get_laplacian()
    

    
