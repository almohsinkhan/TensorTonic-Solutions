import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    #convert to array
    x = np.array(x)

    # find the max logit 
    if x.ndim == 1:
        m = np.max(x)
    else:
        m = np.max(x, axis = 1, keepdims=True)
        
    expo_value = np.exp(x-m)

    if x.ndim == 1:
        expo_sum = np.sum(expo_value)
    else:
        expo_sum = np.sum(expo_value, axis = 1, keepdims=True)
        
    return expo_value/ expo_sum


 
    # calcuate exponential value



     