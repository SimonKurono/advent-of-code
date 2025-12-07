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


if __name__ == "__main__":
    ranges, ids = parse_input("day5/input.txt")
    answer = count_fresh_ids(ranges, ids)
    print(answer)
