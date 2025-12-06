def count_accessible_rolls(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    # 8 directions: (dr, dc)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbor_at_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_at_count += 1

            if neighbor_at_count < 4:
                accessible += 1

    return accessible

"""
Part 2
"""
def count_total_removed(grid):
    grid = [list(row) for row in grid]
    R, C = len(grid), len(grid[0])
    
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    
    def neighbors(r, c):
        count = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '@':
                count += 1
        return count
    
    
    removable = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '@' and neighbors(r, c) < 4:
                removable.add((r, c))
    
    removed_total = 0
    
    
    while removable:
        
        to_remove = list(removable)
        removed_total += len(to_remove)
        
        for r, c in to_remove:
            grid[r][c] = '.'   
        
       
        new_removable = set()
        affected = set()
        
     
        for r, c in to_remove:
            for dr, dc in dirs + [(0,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    affected.add((nr, nc))
        
        
        for r, c in affected:
            if grid[r][c] == '@' and neighbors(r, c) < 4:
                new_removable.add((r, c))
        
        removable = new_removable
    
    return removed_total




if __name__ == "__main__":
    
    with open("day4/input.txt") as f:
         grid = [line.strip() for line in f if line.strip()]


    print(count_accessible_rolls(grid))
    print(count_total_removed(grid))


