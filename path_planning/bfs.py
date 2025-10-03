from collections import deque

def bfs(grid, start, goal):
    h, w = len(grid), len(grid[0])
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        yield ("visit", current)   # 🔵 exploration step

        if current == goal:
            yield ("path", path)   # 🔴 final path
            return

        for dx, dy in moves:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path+[neighbor]))
