from pathlib import Path

boarding_passes = Path('inputs/5.txt').read_text().split('\n')

def seat_id(boarding_pass):
    row, col = boarding_pass[:7], boarding_pass[7:]

    # translation table
    t = str.maketrans({'F': '0', 'B': '1', 'L': '0', 'R': '1'})

    row = int(row.translate(t), base=2)
    col = int(col.translate(t), base=2)

    return row * 8 + col

seat_ids = [seat_id(boarding_pass) for boarding_pass in boarding_passes]

print('part 1:', max(seat_ids))

# part 2
ALL_SEATS = set(range(min(seat_ids), max(seat_ids) + 1))

missing_seat = (ALL_SEATS - set(seat_ids)).pop()

print('part 2:', missing_seat)