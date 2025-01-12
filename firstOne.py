import numpy as np 
# Question number one 
matrix = np.array[
    [1,2,3],
    [4,5,6]
]
def find_matrix_shape(matrix):
    return matrix.shape

# Question number Two 
def computer_cross_product(array1,array2):
    return np.cross(array1,array2)

array1 = np.array[1,2,3]
array2 = np.array[4,5,6]

# Question number three 
B = np.array(
    [[2,3,4],
     [4,5,6]
     [7,8,9]
     ]
)
def reconstruct_matrix(U,S,V):
    return np.linalg.svd(B)
 
    



