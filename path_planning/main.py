import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from grid import create_grid
from astar import astar
from bfs import bfs
from dijkstra import dijkstra

# Grid setup
grid = create_grid(20, 20, obstacle_prob=0.25, seed=42)
start, goal = (0,0), (19,19)

# Choose algorithm
algorithm = "astar"   # "bfs", "dijkstra", "astar"

if algorithm == "astar":
    path = astar(grid, start, goal)
elif algorithm == "bfs":
    path = bfs(grid, start, goal)
elif algorithm == "dijkstra":
    path = dijkstra(grid, start, goal)
else:
    path = None

# Plot grid
fig, ax = plt.subplots()
ax.set_xticks(range(grid.shape[1]))
ax.set_yticks(range(grid.shape[0]))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)

# Show obstacles
for (y,x), value in np.ndenumerate(grid):
    if value == 1:
        ax.add_patch(plt.Rectangle((x,y),1,1,color="black"))

robot_marker, = ax.plot([], [], "ro", markersize=8)

def update(frame):
    if path and frame < len(path):
        x, y = path[frame][1], path[frame][0]
        robot_marker.set_data([x+0.5], [y+0.5])
    return robot_marker,

ani = animation.FuncAnimation(fig, update, frames=len(path), interval=300, repeat=False)
plt.show()
