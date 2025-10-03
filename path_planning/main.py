import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from astar import astar
from grid import create_grid

# --- Settings ---
GRID_SIZE = 20
grid = create_grid(GRID_SIZE, obstacle_prob=0.25, seed=42)
start, goal = (0,0), (GRID_SIZE-1, GRID_SIZE-1)

# --- Matplotlib Setup ---
fig, ax = plt.subplots()
ax.set_xticks(range(GRID_SIZE))
ax.set_yticks(range(GRID_SIZE))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)

# Obstacles
for (y,x), value in np.ndenumerate(grid):
    if value == 1:
        ax.add_patch(plt.Rectangle((x,y),1,1,color="black"))

visited_nodes = []
final_path = []
robot_marker, = ax.plot([], [], "ro", markersize=8)
visited_scat = ax.scatter([], [], c="blue", marker="s", s=100, alpha=0.3)
path_line, = ax.plot([], [], "y-", linewidth=3)  # final yellow path

steps = list(astar(grid, start, goal))

def update(frame):
    global final_path
    action, data = steps[frame]

    if action == "visit":
        visited_nodes.append(data)
        xs = [n[1]+0.5 for n in visited_nodes]
        ys = [n[0]+0.5 for n in visited_nodes]
        visited_scat.set_offsets(np.c_[xs, ys])
        robot_marker.set_data([data[1]+0.5], [data[0]+0.5])

    elif action == "path":
        final_path = data
        xs = [p[1]+0.5 for p in final_path]
        ys = [p[0]+0.5 for p in final_path]
        path_line.set_data(xs, ys)

    return visited_scat, robot_marker, path_line

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=150, repeat=False)
plt.show()
