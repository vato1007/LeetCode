from collections import deque

class Solution:
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        target = (1 << k) - 1

        q = deque()
        q.append((start[0], start[1], 0, energy))

        visited = set()
        visited.add((start[0], start[1], 0, energy))

        moves = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            for _ in range(len(q)):

                r, c, mask, e = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    if (nr, nc) in litter:
                        new_mask |= 1 << litter[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1