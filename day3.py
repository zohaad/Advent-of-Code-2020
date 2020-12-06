from pathlib import Path
from operator import mul
from functools import reduce

tree_map = [[c for c in row] for row in Path('inputs/3.txt').read_text().split('\n')]

tree_count = 0
j = 0 # position
height = len(tree_map)
width = len(tree_map[0])

for i in range(1, height):
    j = (j + 3) % width
    if tree_map[i][j] == '#':
        tree_count += 1

print('part 1:', tree_count)

# part 2

def count_trees(tree_map, right, down):
    tree_count = 0
    j = 0 # starting column position
    height = len(tree_map)
    width = len(tree_map[0])

    for i in range(down, height, down):
        j = (j + right) % width
        if tree_map[i][j] == '#':
            tree_count += 1
    return tree_count

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

print('part 2:', reduce(mul, (count_trees(tree_map, *slope) for slope in slopes)))