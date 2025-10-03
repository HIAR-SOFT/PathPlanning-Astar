from collections import deque

def bfs(grid, start, goal):
    """Breadth-First Search (yields visited cells, then final path)."""
    queue = deque([start])
    came_from = {}
    visited = set([start])

    while queue:
        current = queue.popleft()
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
                grid[neighbor] == 0 and neighbor not in visited):
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
