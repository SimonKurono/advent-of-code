from pathlib import Path

def main():
    pts = []
    for line in Path("day9/input.txt").read_text().splitlines():
        if line:
            x, y = line.split(",")
            pts.append((int(x), int(y)))

    best = 0
    n = len(pts)

    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i + 1, n):
            x2, y2 = pts[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area

    print(best)

if __name__ == "__main__":
    main()
