import re

game_intructions = open('puzzle_input.txt', 'r').read().split('\n')

lines_run = []

def run_line(line, index):
    accumulator = 0
    current_line = index

    if current_line in lines_run:
        print(f'Hit a line we already ran {current_line}')
        return
    else:
        lines_run.append(current_line) 

        parse_line = re.findall('(nop|acc|jmp) (\+|-)(\d+)', line)[0]
        action = parse_line[0]
        symbol = parse_line[1]
        amount = int(parse_line[2])

        if(action == 'nop'):
            current_line += 1
        elif(action == 'acc'):
            if(symbol == '-'):
                accumulator -= amount
                current_line += 1
            elif(symbol == '+'):
                accumulator += amount
                current_line += 1
        elif(action == 'jmp'):
            if(symbol == '-'):
                current_line += - amount
            elif(symbol == '+'):
                current_line += amount
        
        amount = run_line(game_intructions[current_line], current_line)
        if isinstance(amount, int):
            accumulator += amount
    return accumulator

accumulator = run_line(game_intructions[0], 0)
print(f"Part 1 -- {accumulator}")