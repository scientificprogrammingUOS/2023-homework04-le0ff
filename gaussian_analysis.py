import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    #forgive the hardcoding, how could this be solved better?
    if not isinstance(loc, int) and not isinstance(loc, float):
        raise TypeError("Only integers and floats are allowed")
    if not isinstance(scale, int) and not isinstance(scale, float):
        raise TypeError("Only integers and floats are allowed")
    if not isinstance(lower_bound, int) and not isinstance(lower_bound, float):
        raise TypeError("Only integers and floats are allowed")
    if not isinstance(upper_bound, int) and not isinstance(upper_bound, float):
        raise TypeError("Only integers and floats are allowed")
    
    if lower_bound >= upper_bound:
        raise TypeError("lower bound needs to be smaller than upper bound")
    
    #to masking to filter out values below and above the bounds
    gaussian_array = np.random.normal(loc, scale, size=100)
    lower_mask = gaussian_array >= lower_bound
    gaussian_array = gaussian_array[lower_mask]
    upper_mask = gaussian_array <= upper_bound
    gaussian_array = gaussian_array[upper_mask]

    #np functions for mean and std
    return (np.mean(gaussian_array, dtype = np.float64), np.std(gaussian_array, dtype = np.float64))


if __name__ == "__main__":
    # use this for your own testing!
    print(gaussian_analysis(0, 3, 1, 3))
    print(gaussian_analysis(0, 3, 3, 1))
