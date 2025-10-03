import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """A* search (yields visited cells, then final path)."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        yield ("visit", current)

        if current == goal:
            # reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            yield ("path", path)
            return

        y, x = current
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            neighbor = (y+dy, x+dx)
            if (0 <= neighbor[0] < grid.shape[0] and 
                0 <= neighbor[1] < grid.shape[1] and 
                grid[neighbor] == 0):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
