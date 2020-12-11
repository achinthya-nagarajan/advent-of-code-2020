xmas_transmit_raw = open('puzzle_input.txt', 'r').read().split('\n')
xmas_transmit_test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".split('\n')

def encoding_check(encoded_list, preamble):
    current_line = preamble
    while True:
        num = int(encoded_list[current_line])
        num_failed = True
        previous_numbers = []
        for i in range(preamble):
            previous_numbers.append(encoded_list[(current_line - 1) - i])
        for prev_num in previous_numbers:
            for i in range(preamble - 1):
                test = int(prev_num) + int(previous_numbers[i])
                if test == num:
                    num_failed = False
                    current_line += 1
        if num_failed:
            break

    return encoded_list[current_line]

test_preamble = 5
preamble = 25
test_answer = encoding_check(xmas_transmit_test, test_preamble)
p1_answer = encoding_check(xmas_transmit_raw, preamble)
print(f"Test -- Expect: 127 -- Got: {test_answer}")
print(f"Part 1: {p1_answer}")


