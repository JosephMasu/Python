grid = [
    ["S", ".", ".", ".", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", "#", "."],
    [".", "#", ".", ".", "."],
    [".", ".", ".", ".", "E"]
]

start = (0, 0)
end = (4, 4)

queue = [start]
visited = [start]

while queue:
    current = queue.pop(0)

    if current == end:
        print("Path found!")
        break

    row, col = current

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] != "#" and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.append((new_row, new_col))

print(visited)