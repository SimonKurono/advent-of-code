from functools import reduce
import operator

def read_grid(filename="day6/input.txt"):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    lines = [ln for ln in lines if ln.strip() != ""]
    width = max(len(ln) for ln in lines)
    return [ln.ljust(width, " ") for ln in lines]

def find_blocks(grid):
    h = len(grid)
    w = len(grid[0])

    def is_sep(c):
        return all(grid[r][c] == " " for r in range(h))

    blocks = []
    inside = False

    for j in range(w):
        if not inside and not is_sep(j):
            inside = True
            start = j
        elif inside and is_sep(j):
            blocks.append((start, j))
            inside = False

    if inside:
        blocks.append((start, w))

    return blocks

def parse_problem(grid, cs, ce):
    h = len(grid)
    op = next(ch for ch in grid[h - 1][cs:ce] if ch in "+*")
    nums = []
    for r in range(h - 1):
        s = grid[r][cs:ce].strip()
        if s:
            nums.append(int(s))
    return op, nums

def eval_problem(op, nums):
    if op == "+":
        return sum(nums)
    return reduce(operator.mul, nums, 1)

def main():
    grid = read_grid()
    blocks = find_blocks(grid)
    total = 0

    for cs, ce in blocks:
        op, nums = parse_problem(grid, cs, ce)
        total += eval_problem(op, nums)

    print(total)

if __name__ == "__main__":
    main()


#part 2
from functools import reduce
import operator

def read_grid(filename="day6/input.txt"):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]
    lines = [ln for ln in lines if ln.strip() != ""]
    width = max(len(ln) for ln in lines)
    return [ln.ljust(width, " ") for ln in lines]

def find_blocks(grid):
    h = len(grid)
    w = len(grid[0])

    def is_sep(c):
        return all(grid[r][c] == " " for r in range(h))

    blocks = []
    inside = False

    for j in range(w):
        if not inside and not is_sep(j):
            inside = True
            start = j
        elif inside and is_sep(j):
            blocks.append((start, j))
            inside = False

    if inside:
        blocks.append((start, w))

    return blocks

def parse_problem(grid, cs, ce):
    h = len(grid)
    op = next(ch for ch in grid[h - 1][cs:ce] if ch in "+*")
    numbers = []

    for c in range(ce - 1, cs - 1, -1):
        digits = []
        for r in range(h - 1):
            ch = grid[r][c]
            if ch != " ":
                digits.append(ch)
        if digits:
            numbers.append(int("".join(digits)))

    return op, numbers

def eval_problem(op, nums):
    if op == "+":
        return sum(nums)
    return reduce(operator.mul, nums, 1)

def main():
    grid = read_grid()
    blocks = find_blocks(grid)
    total = 0

    for cs, ce in blocks:
        op, nums = parse_problem(grid, cs, ce)
        total += eval_problem(op, nums)

    print(total)

if __name__ == "__main__":
    main()
