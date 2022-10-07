from collections import deque

visit = set()
def DFS(r,c):
    q = deque()
    visit.add((r, c))
    q.append((r,c))

    while q:
        row, col = q.popright()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dr, dc in directions:
            r, c = row + dr, col 
            if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))



