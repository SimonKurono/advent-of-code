def max_joltage_for_bank(line: str) -> int:
    best_tens = int(line[0])  
    best_two_digit = -1
    
    for ch in line[1:]:
        d = int(ch)
        
        candidate = 10 * best_tens + d
        if candidate > best_two_digit:
            best_two_digit = candidate
        
        
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

"""
Part 1 Solution
"""
with open("day3/input.txt") as f:
    lines = f.readlines()

print(total_output_joltage(lines))



"""
Part 2 Solution
"""

def max12(line):
    k = 12
    stack = []
    to_drop = len(line) - k

    for ch in line:
        while stack and to_drop > 0 and stack[-1] < ch:
            stack.pop()
            to_drop -= 1
        stack.append(ch)

    return int("".join(stack[:k]))

total = sum(max12(line.strip()) for line in lines if line.strip())
print(total)

