import math

boarding_pass_raw = open('puzzle_input.txt', 'r').read().split('\n')

def get_seat_ids(boarding_passes):
    seat_ids = []

    for bp in boarding_passes:
        break
        row_min_num = 0
        row_max_num = 127
        row = 0
        col_min_num = 0
        col_max_num = 7
        col = 0

        for i in range(7):
            if(i != 6):
                if bp[i] == 'F':
                    num = math.floor(((row_max_num - row_min_num) / 2))
                    row_max_num = row_max_num - num
                elif bp[i] == 'B':
                    num = math.ceil((row_max_num - row_min_num) / 2)
                    row_min_num = row_min_num + num
            else:
                if bp[i] == 'F':
                    row = row_min_num
                elif bp[i] == 'B':
                    row = row_max_num
        for i in range(4):
            if(i != 3):
                if bp[7 + i] == 'L':
                    num = math.floor((col_max_num - col_min_num) / 2)
                    col_max_num = col_max_num - num
                if bp[7 + i] == 'R':
                    num = math.ceil((col_max_num - col_min_num) / 2)
                    col_min_num = col_min_num + num 
            else: 
                if bp[6 + i] == 'L':
                    col = col_min_num
                elif bp[6 + i] == 'R':
                    col = col_max_num

        seat_id = round(row * 8 + col)
        seat_ids.append(seat_id)
        print(f"{bp}: row {row} col {col} seat ID {round(row * 8 + col)}")

    seat_ids.sort()
    return seat_ids

boarding_pass_test = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
seat_ids = get_seat_ids(boarding_pass_test)
# seat_ids = get_seat_ids(boarding_pass_raw)

# print(f"Part 1 -- Highest Seat ID: {seat_ids[-1]}")
# 839 invalid answer
# 830 invliad answer