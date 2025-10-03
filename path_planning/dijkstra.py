import heapq

def dijkstra(grid, start, goal):
    """Dijkstra’s Algorithm (yields visited cells, then final path)."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    dist = {start: 0}
    visited = set()

    while open_set:
        cost, current = heapq.heappop(open_set)

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
                new_cost = dist[current] + 1
                if new_cost < dist.get(neighbor, float("inf")):
                    dist[neighbor] = new_cost
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (new_cost, neighbor))
