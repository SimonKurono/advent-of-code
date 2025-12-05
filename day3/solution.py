def max_joltage_for_bank(line: str) -> int:
    best_tens = int(line[0])  # largest digit seen so far
    best_two_digit = -1
    
    for ch in line[1:]:
        d = int(ch)
        # form a candidate using best_tens as tens and d as ones
        candidate = 10 * best_tens + d
        if candidate > best_two_digit:
            best_two_digit = candidate
        
        # update the best tens digit so far
        if d > best_tens:
            best_tens = d
    
    return best_two_digit


def total_output_joltage(lines: list[str]) -> int:
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        total += max_joltage_for_bank(line)
    return total


with open("day3/input.txt") as f:
    lines = f.readlines()

print(total_output_joltage(lines))
