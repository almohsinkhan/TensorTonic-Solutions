import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    row_index = np.arange(len(y_true))
    cross_prob = y_pred[row_index, y_true]

    cross_entropy_loss = -np.mean(np.log(cross_prob))

    return  cross_entropy_loss

    