from pathlib import Path
from itertools import combinations
from functools import reduce
from operator import mul

expense_report = [int(expense) for expense in Path("inputs/1.txt").read_text().split('\n')]

for e1, e2 in combinations(expense_report, 2):
    if e1 + e2 == 2020:
        print('part 1:', e1 * e2)

for e1, e2, e3 in combinations(expense_report, 3):
    if e1 + e2 + e3 == 2020:
        print('part 2:', e1 * e2 * e3)

def solution(expense_report, terms):
    # extra credit version
    for c in combinations(expense_report, terms):
        if sum(c) == 2020:
            # print(reduce(lambda a, x: x*a, c))
            print(reduce(mul, c))

solution(expense_report, 2)
solution(expense_report, 3)