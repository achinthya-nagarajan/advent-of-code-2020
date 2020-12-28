import copy

flatten = lambda t: [item for sublist in t for item in sublist]
def pp(LIST):
    for l in LIST:
        print(l)

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

for l in seats_raw.split('\n'):
    seat_line = []
    for c in l:
        seat_line.append(c)
    seat_array.append(seat_line)

copy_of_seats = copy.deepcopy(seat_array)
something_changed = True
amount_of_changes = 0

while something_changed == True:
    if(something_changed == False):
        break
    for line_index, seat_line in enumerate(seat_array):
        for seat_index, seat in enumerate(seat_line):
            if(seat == '.'):
                continue
            adjacent_seats = [
                ["", "", ""],
                ["", "[X]", ""],
                ["", "", ""]
            ]

            if(line_index != 0):
                if(seat_index != 0):
                    adjacent_seats[0][0] = seat_array[line_index - 1][seat_index - 1]
                adjacent_seats[0][1] = seat_array[line_index - 1][seat_index]
                if(seat_index + 1 != len(seat_line)):
                    adjacent_seats[0][2] = seat_array[line_index - 1][seat_index + 1]
            if(seat_index != 0):
                adjacent_seats[1][0] = seat_array[line_index][seat_index - 1]
            if(seat_index + 1 != len(seat_line)):
                adjacent_seats[1][2] = seat_array[line_index][seat_index + 1]
            if(line_index + 1 != len(seat_array)):
                if(seat_index != 0):
                    adjacent_seats[2][0] = seat_array[line_index + 1][seat_index - 1]
                adjacent_seats[2][1] = seat_array[line_index + 1][seat_index]
                if(seat_index + 1 != len(seat_line)):
                    adjacent_seats[2][2] = seat_array[line_index + 1][seat_index + 1]

            flattened = flatten(adjacent_seats)

            if(seat == 'L'):
                if('#' not in flattened):
                    copy_of_seats[line_index][seat_index] = '#'
            elif(seat == '#'):
                if(flattened.count('#') >= 4):
                    copy_of_seats[line_index][seat_index] = 'L'
    amount_of_changes += 1

    # print(f"LAYOUT: {amount_of_changes} ----------------------------")
    # pp(copy_of_seats)

    if(seat_array == copy_of_seats):
        something_changed = False
    else:
        seat_array = copy.deepcopy(copy_of_seats)

occupied_seats = flatten(seat_array).count('#')
print(f"""Part 1 Answer: {occupied_seats}""")