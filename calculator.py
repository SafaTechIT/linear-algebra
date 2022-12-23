import numpy as np



def calculator(A, B):
    array = augmented(A=A, B=B.T)
    array = echelon(array)
    array = reduction_form(array)
	               
    if is_consist(array):
        print("--> System is inconsistent")
        return

    print("--> Equetions: ")
    pvt = pvt_finder(array)
    print()

    print("--> Variable: ")
    for i in range(array.shape[1]-1):
        if i in pvt:
            print("\tVariable x" + str(i+1) + " is not free")
        else:
            print("\tVariable x" + str(i+1) + " is free")
  

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
    print("--> A Matrix: ")
    print(coefficient)
    print()
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
    print("--> B Vector: ")
    print(vector)
    print()
    return vector

if __name__ == "__main__":
    A = get_A_matrix()
    B = get_B_vector()
    calculator(A, B)


def augmented(A, B):
    array = np.append(A, B, axis=1)
    printer(array, typ="Augmented")
    return array         

def printer(array, typ):
    print(f"--> {typ} Form: ")
    print(array)
    print()

def echelon(A):
    row, column = A.shape

    array = None

    if row == 0 or column == 0:
        array = A
        printer(array, typ="Echelon")
        return array

    for i in range(len(A)):
        if A[i, 0] != 0:
            break
    else:
        B = echelon(A[:, 1:])
        array = np.hstack([A[:, :1], B])
        printer(array, typ="Echelon")
        return array

    if i > 0:
        temp_row = A[i].copy()
        A[i] = A[0]
        A[0] = temp_row
    
    temp = np.array((A[0] / A[0,0]), dtype=A.dtype)
    A[1:] -= temp * A[1:, 0:1]

    B = echelon(A[1:, 1:])
    array = np.vstack([A[:1], np.hstack([A[1:, :1], B])])
    printer(array, typ="Echelon")
    return array



def reduction_form(A):
    row, column = A.shape
    
    if row == 0:
        return A
        
    for i in range(column):
        if A[-1, i] != 0:
            break
    else:
        B = reduction_form(A[:-1,:])
        return np.vstack([B, A[-1:, :]])
        
    A[-1] = A[-1] / A[-1, i]
    A[:-1, :] -= A[-1] * A[:-1, :]

    B = reduction_form(A[:-1,:])
    array = np.vstack([B, A[-1:, :]])
    print("--> Reduction Echelon Form: ")
    print(array)
    print()
    return array

def is_consist(A):
    row, column = A.shape
    for i in range(row):
        flag = True
        for j in range(column - 1):
            if A[i,j] != 0:
                flag = False
        if flag and A[i, j + 1] != 0:
            return True
    return False



def pvt_finder(A):
    pvt = []
    row, column = A.shape
    for i in range(row):
        line = []
        flag = True
        for j in range(column-1):
            if A[i,j] != 0:
                if A[i,j] == 1:
                    line.append("x" + str(j+1))
                else:
                    string = '({:.3f})x{}'.format(A[i,j], j+1)
                    line.append(string)
                if flag:
                    pvt.append(j)
                flag = False
        if len(line) == 0:
            continue
        formul = " + ".join(line)
        formul += " = " + '{:.3f}'.format(A[i,column-1])
        print(formul)
    return pvt