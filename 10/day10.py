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

joltage_test_large = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')

converted_voltage = []

for j in joltage_raw:
    converted_voltage.append(int(j))
    
converted_voltage.sort()
differences = [0, 0, 0]

# Add our first difference
differences[converted_voltage[0] - 1] += 1

for i, v in enumerate(converted_voltage):
    # print("------------")
    # print(f"{v}")
    if(i != len(converted_voltage) - 1):
        difference = converted_voltage[i + 1] - v
        if(difference > 3):
            print(v, converted_voltage[i + 1])
            print("Bigger difference than 3")
            break
        differences[difference - 1] += 1
        # print(f"+{difference}")
    else:
        difference = converted_voltage[i] - v
        differences[difference - 1] += 1
        # print(f"+{difference}")

print(differences)
print(differences[0] * differences[2])

