import re

baggage_regulations_raw = open('puzzle_input.txt', 'r').read().split('\n')

def parse_regulation(regulation):
    match = re.findall("([a-z]+ [a-z]+) bags contain (.+)$", regulation)[0]
    value = match[0]
    next_values = match[1].replace('.', '').split(',')
    if(next_values == 'no other bags'):
        next_values = None

    return value, next_values

def check_regulations(baggage_regulations):
    regulations_tree = {}
    for regulation in baggage_regulations_raw:
        value, next_values = parse_regulation(regulation)
        regulations_tree[value] = next_values

    return regulations_tree

regulations_tree = check_regulations(baggage_regulations_raw)

def pretty_print(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty_print(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

pretty_print(regulations_tree, 1)