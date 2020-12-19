joltage_raw = open('puzzle_input.txt', 'r').read().split('\n')

joltage_test_small = """16
10
15
5
1
11
7
19
6
12
4""".split('\n')

converted_voltage = []

for j in joltage_raw:
    converted_voltage.append(int(j))
    
converted_voltage.sort()
differences = [0, 0, 0]

# Add our first difference
differences[converted_voltage[0] - 1] += 1

for i, v in enumerate(converted_voltage):
    if(i != len(converted_voltage) - 1):
        difference = converted_voltage[i + 1] - v
        differences[difference - 1] += 1
    else:
        # Last one
        difference = converted_voltage[i] - converted_voltage[i] + 3
        differences[difference - 1] += 1

print(f"Part 1: {differences[0] * differences[2]}")

