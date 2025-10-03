import heapq

def astar(grid, start, goal):
    h, w = len(grid), len(grid[0])
    moves = [(0,1), (1,0), (0,-1), (-1,0)]  # 4 directions

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])  # Manhattan distance

    open_set = []
    heapq.heappush(open_set, (0+heuristic(start,goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)

        for dx, dy in moves:
            nx, ny = current[0]+dx, current[1]+dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 0:
                heapq.heappush(open_set, (g+1+heuristic((nx,ny),goal), g+1, (nx,ny), path+[(nx,ny)]))
    return None
