import sys
from collections import defaultdict

def solve_part1(lines, start_r, start_c):
    total_splits = 0
    active_beams = {start_c}
    height = len(lines)
    
    for r in range(start_r, height):
        row_str = lines[r]
        width = len(row_str)
        next_beams = set()
        
        for c in active_beams:
            if c < 0 or c >= width:
                continue
            
            if row_str[c] == '^':
                total_splits += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)
            else:
                next_beams.add(c)
        
        active_beams = next_beams
        if not active_beams:
            break
            
    return total_splits

def solve_part2(lines, start_r, start_c):
    timelines = defaultdict(int)
    timelines[start_c] = 1
    finished_timelines = 0
    height = len(lines)
    
    for r in range(start_r, height):
        row_str = lines[r]
        width = len(row_str)
        next_timelines = defaultdict(int)
        
        for c, count in timelines.items():
            if c < 0 or c >= width:
                finished_timelines += count
                continue
            
            if row_str[c] == '^':
                next_timelines[c - 1] += count
                next_timelines[c + 1] += count
            else:
                next_timelines[c] += count
        
        timelines = next_timelines
    
    finished_timelines += sum(timelines.values())
    return finished_timelines

def main():
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

    p1 = solve_part1(lines, start_r, start_c)
    print(f"Part 1 Answer: {p1}")

    p2 = solve_part2(lines, start_r, start_c)
    print(f"Part 2 Answer: {p2}")

if __name__ == '__main__':
    main()