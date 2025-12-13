from math import prod
import heapq

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.s = [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a = self.find(a); b = self.find(b)
        if a == b: return
        if self.s[a] < self.s[b]: a, b = b, a
        self.p[b] = a
        self.s[a] += self.s[b]

pts = []
with open("day8/input.txt") as f:
    for line in f:
        if line.strip():
            pts.append(tuple(map(int, line.split(","))))

n = len(pts)
pairs = []
for i in range(n):
    x1, y1, z1 = pts[i]
    for j in range(i+1, n):
        x2, y2, z2 = pts[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        pairs.append((dx*dx + dy*dy + dz*dz, i, j))

closest = heapq.nsmallest(1000, pairs, key=lambda t: t[0])
closest.sort(key=lambda t: t[0])

dsu = DSU(n)
for _, i, j in closest:
    dsu.union(i, j)

cnt = {}
for i in range(n):
    r = dsu.find(i)
    cnt[r] = cnt.get(r, 0) + 1

sizes = sorted(cnt.values(), reverse=True)
print(prod(sizes[:3]))
