import heapq

def astar(grid, start, goal):
    h, w = len(grid), len(grid[0])
    moves = [(0,1),(1,0),(0,-1),(-1,0)]

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

    open_set = [(0+heuristic(start,goal), 0, start, [start])]
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        # 🔵 Yield each visited node during search
        yield ("visit", current)

        if current == goal:
            # 🔴 When found, yield the final path
            yield ("path", path)
            return

        for dx, dy in moves:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
                heapq.heappush(open_set,
                               (cost+1+heuristic((nx,ny),goal), cost+1, (nx,ny), path+[(nx,ny)]))
