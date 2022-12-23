import numpy as np

def get_A_matrix():
    print("Please enter your 3x3 matrix like: i,i,i + j,j,j + k,k,k ")
    d = input("For spliting\n")
    a = d.split(" + ")
    coefficient = list()
    for i in a:
        node = i.split(",")
        maker = list()
        for j in node:
            maker.append(int(j))
        coefficient.append(maker)

    coefficient = np.array(coefficient, dtype=np.float64)
    return coefficient

def get_B_vector():
    print("Please enter your 3x1 vector like: i,i,i")
    d = input("For spliting\n")
    node = d.split(",")
    maker, vector = list(), list()
    for j in node:
        maker.append(int(j))
    vector.append(maker)
    vector = np.array(vector, dtype=np.float64)
    return vector


# array = np.array([[0,1,-4], [2,-3,2], [5,-8,7]], dtype = np.float64)
# print(">> A Matrix: ")
# print(array)
# print("    ----    \n")

# z = np.array([[8,1,1]], dtype=array.dtype).T
# print(">> b Vector: ")
# print(z)
# print("    ----    \n")

# print(np.linalg.solve(array, z))