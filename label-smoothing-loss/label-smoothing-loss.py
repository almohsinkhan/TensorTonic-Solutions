import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    # Write code here
    k = len(predictions)
    loss = 0.0

    uniform_prob = epsilon / k

    for i, p in enumerate(predictions):
        target_prob = uniform_prob
        if i == target:
            target_prob += (1.0 - epsilon)

        loss -= target_prob * math.log(p)

    return loss