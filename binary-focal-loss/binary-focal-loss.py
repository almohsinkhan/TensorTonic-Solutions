import math

def binary_focal_loss(predictions: list, targets: list, alpha: float, gamma: float) -> float:
    """
    Returns the mean binary focal loss as a float.
    """
    pt = []
    for i in range(len(targets)):
        if targets[i] == 1:
            pt.append(predictions[i])
        else:
            pt.append(1-predictions[i])

    ft = []

    for i in range(len(targets)):
        f = (-alpha*((1-pt[i])**gamma))*(math.log(pt[i]))
        ft.append(f)


    return sum(ft)/len(ft)

            
    
            