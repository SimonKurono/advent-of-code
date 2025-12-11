def solve():
    try:
        with open('day7/input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("Error: input.txt file not found.")
        return

    if not lines:
        return

    start_r, start_c = -1, -1
    for r, line in enumerate(lines):
        if 'S' in line:
            start_r = r
            start_c = line.find('S')
            break
    
    if start_r == -1:
        return

    active_beams = {start_c}
    total_splits = 0
    height = len(lines)

    for r in range(start_r, height):
        row_str = lines[r]
        width = len(row_str)
        next_beams = set()
        
        for c in active_beams:
            if c < 0 or c >= width:
                continue
            
            char = row_str[c]
            
            if char == '^':
                total_splits += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            else:
                next_beams.add(c)
        
        active_beams = next_beams
        
        if not active_beams:
            break

    print(f"Answer: {total_splits}")

if __name__ == '__main__':
    solve()