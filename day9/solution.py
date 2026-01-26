from pathlib import Path
from bisect import bisect_left

def prefix2d(a):
    h = len(a)
    w = len(a[0]) if h else 0
    ps = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(h):
        row_ps = ps[y + 1]
        prev_ps = ps[y]
        s = 0
        for x in range(w):
            s += a[y][x]
            row_ps[x + 1] = prev_ps[x + 1] + s
    return ps

def rect_sum(ps, x1, y1, x2, y2):
    return ps[y2][x2] - ps[y1][x2] - ps[y2][x1] + ps[y1][x1]

def main():
    pts = []
    for line in Path("day9/input.txt").read_text().splitlines():
        line = line.strip()
        if line:
            x, y = map(int, line.split(","))
            pts.append((x, y))

    n = len(pts)

    best1 = 0
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i + 1, n):
            x2, y2 = pts[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best1:
                best1 = area

    Xs = set()
    Ys = set()
    for x, y in pts:
        Xs.add(x)
        Xs.add(x + 1)
        Ys.add(y)
        Ys.add(y + 1)

    X = sorted(Xs)
    Y = sorted(Ys)
    wx = len(X) - 1
    hy = len(Y) - 1

    x_index = {v: i for i, v in enumerate(X)}
    y_index = {v: i for i, v in enumerate(Y)}

    v_edges = []
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if x1 == x2:
            ya, yb = (y1, y2) if y1 < y2 else (y2, y1)
            v_edges.append((x1, ya, yb))

    inside = [[0] * wx for _ in range(hy)]
    for j in range(hy):
        ymid = (Y[j] + Y[j + 1]) / 2.0
        xs = []
        for x, ya, yb in v_edges:
            if ya <= ymid < yb:
                xs.append(x)
        xs.sort()
        for k in range(0, len(xs), 2):
            if k + 1 >= len(xs):
                break
            a = xs[k]
            b = xs[k + 1]
            if a > b:
                a, b = b, a
            ia = bisect_left(X, a)
            ib = bisect_left(X, b)
            for i in range(ia, ib):
                inside[j][i] = 1

    ps_inside = prefix2d(inside)

    best2 = 0
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i + 1, n):
            x2, y2 = pts[j]
            lx, rx = (x1, x2) if x1 <= x2 else (x2, x1)
            ly, ry = (y1, y2) if y1 <= y2 else (y2, y1)
            area = (rx - lx + 1) * (ry - ly + 1)
            if area <= best2:
                continue
            ix1 = x_index[lx]
            ix2 = x_index[rx + 1]
            iy1 = y_index[ly]
            iy2 = y_index[ry + 1]
            cells = (ix2 - ix1) * (iy2 - iy1)
            if cells <= 0:
                continue
            if rect_sum(ps_inside, ix1, iy1, ix2, iy2) == cells:
                best2 = area

    print(best1)
    print(best2)

if __name__ == "__main__":
    main()
