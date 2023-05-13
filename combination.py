import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    arr1 = arr1.squeeze()
    arr2 = arr2.squeeze()
    try:
        result = np.concatenate((arr1, arr2), axis = axis)
        return result
    except:
        raise TypeError(f"Combination is not possible through axis {axis}")


if __name__ == "__main__":
    arr1 = np.arange(6).reshape(2, 3)
    print("Array1: ")
    print(arr1)
    arr2 = np.ones((2,2))
    print("Array2: ")
    print(arr2)
    
    print(combination(arr1, arr2, 1))
