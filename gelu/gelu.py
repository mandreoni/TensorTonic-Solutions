import numpy as np
import math

def gelu(arr):
    arry = np.asanyarray(arr, dtype=float)
    
    # Define a scalar function first
    scalar_erf = lambda x: math.erf(x / math.sqrt(2))
    
    # Vectorize the scalar function
    vectorized_erf = np.vectorize(scalar_erf)
    
    return 0.5 * arry * (1.0 + vectorized_erf(arry))