import re

baggage_regulations_raw = open('puzzle_input.txt', 'r').read().split('\n')

def parse_regulations(baggage_regulations):
    regulations_tree = {}
    for regulations in baggage_regulations_raw:
        print(regulations)
        match = re.findall("([a-z]+ [a-z]+) bags contain (.+)$", regulations)[0]
        regulations_tree[match[0]] = None
        print(match[1].split(','))
        break

    print(regulations_tree)
parse_regulations(baggage_regulations_raw)