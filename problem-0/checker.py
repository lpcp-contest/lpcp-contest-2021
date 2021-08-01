#!/usr/bin/env python3

"""
Example input:

6
3 1 2 5 1 1
1 3 1 1 3 4
1 1 1 2 3 3
1 3 1 2 3 3
1 3 3 3 3 4
5 4 4 3 4 4
5 5 4 3 4 4
6 6 4 4 4 4
...*..
*.**..
*.....
...*..
**.*..
..****
"""

import sys


def pretty_print(columns, rows, grid, filled):
    for i in range(len(grid)):
        l = []
        for j in range(len(grid)):
            l.append(chr((ord('A') if filled[i][j] else ord('a')) + grid[i][j] - 1))
        l.append(f' {rows[i]}')
        print(''.join(l))

    l = []
    for i in range(len(grid)):
        l.append(str(columns[i] // 10) if columns[i] > 9 else ' ')
    print(''.join(l))

    l = []
    for i in range(len(grid)):
        l.append(str(columns[i] % 10))
    print(''.join(l))

    print()


size = int(input())
columns = [int(x) for x in input().split()]
rows = [int(x) for x in input().split()]

grid = []
for _ in range(size):
    grid.append([int(x) for x in input().split()])

filled = []
for _ in range(size):
    line = input()
    if len(line) != size:
        sys.exit(f"Wrong length of row {len(filled)+1}.")
    if not all(x in ['.', '*'] for x in line):
        sys.exit(f"Row {len(filled)+1} contains unexpected chars.")
    filled.append([1 if x == '*' else 0 for x in line])

pretty_print(columns, rows, grid, filled)

for i in range(size):
    if rows[i] != sum(filled[i]):
        sys.exit(f"Clue on row {i+1} is unsatisfied.")
    if columns[i] != sum(filled[j][i] for j in range(size)):
        sys.exit(f"Clue on column {i+1} is unsatisfied.")

for i in range(size):
    for j in range(size):
        if not filled[i][j]:
            continue
        if i+1 < len(grid) and grid[i][j] == grid[i+1][j] and not filled[i+1][j]:
            sys.exit(f"Gravity unsatisfied at row {i+1} and column {j+1}.")
        for j_ in range(size):
            if grid[i][j] == grid[i][j_] and not filled[i][j_]:
                sys.exit(f"Partially filled at row {i+1}: water in column {j+1} but not in column {j_+1}.")

print("CORRECT!")
