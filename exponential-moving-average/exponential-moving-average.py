def exponential_moving_average(values: list, alpha: float) -> list:
    """Returns the exponential moving average at every position."""
    if not values:
        return []
    
    ema = []
    current_ema = values[0]
    ema.append(current_ema)
    
    for val in values[1:]:
        current_ema = alpha * val + (1 - alpha) * current_ema
        ema.append(current_ema)
        
    return ema
