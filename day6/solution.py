from functools import reduce
import operator

def read_grid(filename="day6/input.txt"):
    with open(filename, "r") as f:
        # Keep trailing spaces (important!), just strip newline
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Remove completely empty lines if any (optional/safe)
    lines = [ln for ln in lines if ln.strip() != ""]

    width = max(len(ln) for ln in lines)
    # Pad all lines to same width with spaces on the right
    padded = [ln.ljust(width, " ") for ln in lines]
    return padded  # list of strings, each same length


def find_problem_columns(grid):
    """
    Returns a list of (start, end) column indices (end exclusive),
    each representing one vertical problem block.
    """
    h = len(grid)
    w = len(grid[0])

    # A separator column is all spaces
    def is_separator(col):
        return all(grid[row][col] == " " for row in range(h))

    blocks = []
    inside = False
    start = 0

    for j in range(w):
        sep = is_separator(j)
        if not inside and not sep:
            # We are entering a new problem block
            inside = True
            start = j
        elif inside and sep:
            # We are leaving a problem block
            blocks.append((start, j))
            inside = False

    # If we ended still inside a block, close it
    if inside:
        blocks.append((start, w))

    return blocks


def parse_problem(grid, col_start, col_end):
    """
    For a single vertical block [col_start, col_end),
    extract the operator from the last row and the numbers
    from rows above.
    """
    h = len(grid)

    # Operator is in the last row within [col_start, col_end)
    last_row = grid[h - 1][col_start:col_end]
    op_char = None
    for ch in last_row:
        if ch in "+*":
            op_char = ch
            break
    if op_char is None:
        raise ValueError(f"No operator found in columns {col_start}-{col_end}")

    # Extract numbers from rows 0..h-2
    nums = []
    for r in range(h - 1):
        slice_str = grid[r][col_start:col_end]
        s = slice_str.strip()
        if s:  # non-empty
            nums.append(int(s))

    if not nums:
        raise ValueError(f"No numbers found for problem in columns {col_start}-{col_end}")

    return op_char, nums


def eval_problem(op_char, nums):
    if op_char == "+":
        return sum(nums)
    elif op_char == "*":
        return reduce(operator.mul, nums, 1)
    else:
        raise ValueError(f"Unknown operator: {op_char}")


def main():
    grid = read_grid("day6/input.txt")
    blocks = find_problem_columns(grid)

    total = 0
    for (cs, ce) in blocks:
        op, nums = parse_problem(grid, cs, ce)
        result = eval_problem(op, nums)
        total += result

    print(total)


if __name__ == "__main__":
    main()
