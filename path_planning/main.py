import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.animation as animation
import numpy as np
from astar import astar
from bfs import bfs
from dijkstra import dijkstra

GRID_SIZE = 20
START = (0, 0)
GOAL = (GRID_SIZE - 1, GRID_SIZE - 1)
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)  # space for buttons
ax.set_xticks(np.arange(0, GRID_SIZE, 1))
ax.set_yticks(np.arange(0, GRID_SIZE, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(True)

# Draw start and goal
ax.add_patch(plt.Rectangle((START[1], START[0]), 1, 1, color="green"))
ax.add_patch(plt.Rectangle((GOAL[1], GOAL[0]), 1, 1, color="red"))

# Grid patches
patches = [[None]*GRID_SIZE for _ in range(GRID_SIZE)]

def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if patches[y][x]:
                patches[y][x].remove()
                patches[y][x] = None
            if grid[y, x] == 1:
                rect = plt.Rectangle((x, y), 1, 1, color="black")
                ax.add_patch(rect)
                patches[y][x] = rect
    fig.canvas.draw_idle()

def onclick(event):
    if event.inaxes != ax:
        return
    x, y = int(event.xdata), int(event.ydata)
    if (y, x) == START or (y, x) == GOAL:
        return
    grid[y, x] = 0 if grid[y, x] == 1 else 1
    draw_grid()

fig.canvas.mpl_connect('button_press_event', onclick)
draw_grid()

# HUD
hud_text = ax.text(0, -1, "", fontsize=12, color="purple", va="top")

# Robot and path objects
robot_marker, visited_points, path_line = None, None, None
visited_x, visited_y, final_path = [], [], []
ani = None  # keep animation alive

def run_algorithm(algo_name):
    global robot_marker, visited_points, path_line, visited_x, visited_y, final_path, grid, ani

    visited_x, visited_y, final_path = [], [], []

    grid[START] = 0
    grid[GOAL] = 0

    if algo_name == "ASTAR":
        steps = list(astar(grid, START, GOAL))
    elif algo_name == "BFS":
        steps = list(bfs(grid, START, GOAL))
    elif algo_name == "DIJKSTRA":
        steps = list(dijkstra(grid, START, GOAL))
    else:
        return

    # Clear previous lines if any
    if robot_marker: robot_marker.remove()
    if visited_points: visited_points.remove()
    if path_line: path_line.remove()

    robot_marker, = ax.plot([], [], "bo", markersize=8)
    visited_points, = ax.plot([], [], "yo", markersize=4, alpha=0.6)
    path_line, = ax.plot([], [], "b-", linewidth=2)

    max_possible = GRID_SIZE * GRID_SIZE

    def update(frame):
        global final_path
        kind, data = steps[frame]

        if kind == "visit":
            y, x = data
            visited_x.append(x + 0.5)
            visited_y.append(y + 0.5)
            visited_points.set_data(visited_x, visited_y)
            robot_marker.set_data([x + 0.5], [y + 0.5])
        elif kind == "path":
            final_path = data
            px = [x + 0.5 for (_, x) in final_path]
            py = [y + 0.5 for (y, _) in final_path]
            path_line.set_data(px, py)

        explored = len(visited_x)
        path_len = len(final_path)
        score = max(0, int(100 * (1 - (explored*0.5 + path_len*1)/max_possible)))
        hud_text.set_text(f"Algorithm: {algo_name} | Cells: {explored} | Path: {path_len} | Score: {score}/100")
        return visited_points, robot_marker, path_line, hud_text

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=50, repeat=False)
    plt.draw()

def restart(event=None):
    global grid, visited_x, visited_y, final_path
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    visited_x, visited_y, final_path = [], [], []
    draw_grid()
    hud_text.set_text("")

# Algorithm buttons
btn_astar = Button(plt.axes([0.05, 0.05, 0.2, 0.075]), "A* Search", color="lightblue", hovercolor="skyblue")
btn_astar.on_clicked(lambda event: run_algorithm("ASTAR"))

btn_bfs = Button(plt.axes([0.35, 0.05, 0.2, 0.075]), "BFS", color="lightgreen", hovercolor="green")
btn_bfs.on_clicked(lambda event: run_algorithm("BFS"))

btn_dij = Button(plt.axes([0.65, 0.05, 0.2, 0.075]), "Dijkstra", color="lightcoral", hovercolor="red")
btn_dij.on_clicked(lambda event: run_algorithm("DIJKSTRA"))

btn_restart = Button(plt.axes([0.85, 0.05, 0.1, 0.075]), "Restart", color="orange", hovercolor="red")
btn_restart.on_clicked(restart)

plt.title("Click cells to toggle obstacles")
plt.show()
