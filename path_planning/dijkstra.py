import heapq

def dijkstra(grid, start, goal):
    h, w = len(grid), len(grid[0])
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    open_set = [(0, start, [start])]
    visited = set()

    while open_set:
        cost, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        yield ("visit", current)   #  exploration step

        if current == goal:
            yield ("path", path)   # final path
            return

        for dx, dy in moves:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                heapq.heappush(open_set, (cost+1, neighbor, path+[neighbor]))
