from collections import deque
from typing import List

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def bfs(src):
            dist = [-1] * n
            dist[src] = 0
            q = deque([src])

            while q:
                u = q.popleft()

                for v in g[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)

            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        ans = 0

        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])

            if a * a + b * b == c * c:
                ans += 1

        return ans