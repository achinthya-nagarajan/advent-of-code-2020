bus_times = open('puzzle_input.txt').read().split('\n')

earliest_departure_time = int(bus_times[0])
bus_ids = []

for bus_id in bus_times[1].split(','):
    if bus_id == 'x':
        continue
    else:
        bus_ids.append(int(bus_id))

earliest_times = {}

# print(earliest_departure_time)

for count, item in enumerate(bus_ids):
    amount = 0
    while amount < earliest_departure_time:
        amount += item * (count + 1)
    earliest_times[item] = amount

earliest_time = earliest_times[bus_ids[0]] - earliest_departure_time
answer = 0

print(earliest_time)

for count, time in enumerate(earliest_times):
    if count != 0 and count != len(earliest_times):
        t1 = earliest_times[time] - earliest_departure_time
        if t1 < earliest_time:
            earliest_time = time
            answer = time * t1

print(f"Part 1: {answer}")

