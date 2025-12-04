def count_part1(rotations):
    """Count how many times the dial is at 0 AFTER a rotation."""
    pos = 50
    count = 0
    for line in rotations:
        d = line[0]
        dist = int(line[1:])
        if d == 'R':
            pos = (pos + dist) % 100
        else:
            pos = (pos - dist) % 100
        if pos == 0:
            count += 1
    return count


def count_part2(rotations):
    """
    Count how many times any *click* lands on 0, including intermediate ones.
    Dial positions are 0..99, starting at 50.
    """
    pos = 50
    count = 0

    for line in rotations:
        d = line[0]
        dist = int(line[1:])

        # intermediate hits:
        # R: (pos + k) % 100 == 0  -> k ≡ -pos (mod 100)
        # L: (pos - k) % 100 == 0  -> k ≡  pos (mod 100)
        if d == 'R':
            k0 = (-pos) % 100
        else:
            k0 = (pos) % 100

        # k must be positive; if k0 == 0, first positive is 100
        if k0 == 0:
            k0 = 100

        if k0 <= dist:
            count += 1 + (dist - k0) // 100

        # update position
        if d == 'R':
            pos = (pos + dist) % 100
        else:
            pos = (pos - dist) % 100

    return count


def main():
    with open("day2/input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    part1 = count_part1(rotations)
    part2 = count_part2(rotations)

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
