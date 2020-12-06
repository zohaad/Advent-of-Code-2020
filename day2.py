from pathlib import Path

lines = Path("inputs/2.txt").read_text().split("\n")


def destruct(line):
    policy, password = line.split(": ")
    counts, letter = policy.split(" ")
    min_count, max_count = map(int, counts.split("-"))

    return password, letter, min_count, max_count


def valid(line):
    # destruct
    password, letter, min_count, max_count = destruct(line)

    # check if valid password
    return min_count <= password.count(letter) <= max_count


def valid2(line):
    password, letter, a, b = destruct(line)
    return (password[a - 1] == letter) ^ (password[b - 1] == letter)


print("part 1:", sum(map(valid, lines)))
print("part 2:", sum(map(valid2, lines)))
