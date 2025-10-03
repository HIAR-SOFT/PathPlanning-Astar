import numpy as np

def create_grid(width, height, obstacle_prob=0.3, seed=None):
    """Create a grid world with random obstacles."""
    if seed is not None:
        np.random.seed(seed)
    grid = np.zeros((height, width), dtype=int)

    for y in range(height):
        for x in range(width):
            if np.random.rand() < obstacle_prob:
                grid[y, x] = 1  # obstacle
    return grid
