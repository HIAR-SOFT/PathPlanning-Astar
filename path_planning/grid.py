import numpy as np

def create_grid(width=20, height=20, obstacle_prob=0.2, seed=None):
    if seed:
        np.random.seed(seed)
    grid = np.zeros((height, width), dtype=int)
    # randomly add obstacles
    for y in range(height):
        for x in range(width):
            if np.random.rand() < obstacle_prob:
                grid[y, x] = 1
    return grid

#0-free space     1-obstacle