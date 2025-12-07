from bisect import bisect_right

def parse_input(filename):
    ranges = []
    ids = []

    with open(filename, "r") as f:
        mode = "ranges"
        for line in f:
            line = line.strip()

            if line == "":
                mode = "ids"
                continue

            if mode == "ranges":
                a, b = line.split("-")
                ranges.append((int(a), int(b)))
            else:
                ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


def count_fresh_ids(ranges, ids):
    merged = merge_ranges(ranges)

    starts = [s for s, e in merged]
    ends   = [e for s, e in merged]

    fresh_count = 0

    for x in ids:
        i = bisect_right(starts, x) - 1
        if i >= 0 and x <= ends[i]:
            fresh_count += 1

    return fresh_count



"""
Part 2 Solution
"""

def parse_ranges(filename: str):
    ranges = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":      # stop at blank line; after this are IDs we don't care about
                break
            a, b = line.split("-")
            ranges.append((int(a), int(b)))
    return ranges


def merge_ranges(ranges):
    """Merge overlapping [start, end] intervals."""
    if not ranges:
        return []

    ranges.sort()  # sort by start, then end
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # overlap
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


def count_fresh_ids_from_ranges(filename: str) -> int:
    ranges = parse_ranges(filename)
    merged = merge_ranges(ranges)
    # sum of lengths of merged intervals
    total = sum(end - start + 1 for start, end in merged)
    return total



    


if __name__ == "__main__":
    ranges, ids = parse_input("day5/input.txt")
    answer = count_fresh_ids(ranges, ids)
    print(answer)

    ans = count_fresh_ids_from_ranges("day5/input.txt")
    print(ans)
