from pathlib import Path

groups = [
    [set(question) for question in group.split("\n")]
    for group in Path("inputs/6.txt").read_text().split("\n\n")
]

print("part 1:", sum(len(set.union(*group)) for group in groups))
print("part 2:", sum(len(set.intersection(*group)) for group in groups))
