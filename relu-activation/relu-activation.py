import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    result = np.clip(x, a_min=0, a_max=None)
    
    return result