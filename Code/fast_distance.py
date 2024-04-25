from numba import jit
import numpy as np

# Custom Numba Functions to calculate the arccos distance quickly
@jit(nopython=True)
def custom_clip(x, min_val, max_val):
    if x < min_val:
        return min_val
    elif x > max_val:
        return max_val
    else:
        return x

@jit(nopython=True)
def arccos_distance(x, y):
    """Compute arccos distance between two points."""
    x = x.astype(np.float64)
    y = y.astype(np.float64)
    norm_x = np.sqrt(np.sum(x ** 2))
    norm_y = np.sqrt(np.sum(y ** 2))
    cosine_similarity = np.dot(x, y) / (norm_x * norm_y)
    angle = np.arccos(custom_clip(cosine_similarity, -1, 1))
    return angle