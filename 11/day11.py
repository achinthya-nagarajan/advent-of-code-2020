seats_raw = open('puzzle_input.txt').read()

seats_test = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

seat_array = []

for l in seats_test.split('\n'):
    seat_array.append(l)

for seat_line in seat_array:
    for seat in seat_line:
        seat_status = 0
            for seat_line in seat_array:
                for seat in seat_line:

