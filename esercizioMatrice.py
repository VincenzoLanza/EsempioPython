import numpy as np

matrice=np.zeros((10,10))


for i in range(matrice.shape[0]):
    for j in range(matrice.shape[1]):
        if i == j:
            matrice[i,j] =i
print(matrice)
