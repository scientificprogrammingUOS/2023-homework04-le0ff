import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    arr = np.zeros(shape, dtype=bool)
    arr[::3, ::3] = True
    arr[1::3, 2::3] = True
    arr[2::3, 1::3] = True
    return arr


if __name__ == "__main__":
    print(strange_pattern((2,2)))
    print("---------")
    print(strange_pattern((10, 10)))
    
