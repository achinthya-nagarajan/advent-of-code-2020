import re

baggage_regulations_raw = open('puzzle_input.txt', 'r').read().split('\n')
baggage_regulations_test = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")

def build_regulation_tree(baggage_regulations_raw):
   regulation_tree = {}
   for regulation in baggage_regulations_raw:
      sub_tree = {}
      match = re.findall("([a-z]+ [a-z]+) bags contain (.+)$", regulation)[0]
      value = match[0]
      nested_bags = match[1].replace('.', '').split(",")
      for nb in nested_bags:
         if(nb != 'no other bags'):
            sub_match = re.findall("(\d+) ([a-z]+ [a-z]+) bags?", nb)[0]
            amount = sub_match[0]
            sub_value = sub_match[1]
            sub_tree[sub_value] = None
         else:
            sub_tree = 'End' 
         regulation_tree[value] = sub_tree

   return regulation_tree

def parse_regulations(regulation_tree):
   parsed_tree = regulation_tree

   for bag, values in parsed_tree.items():
      if(values == 'End'):
         continue
      else:
         for v in values:
            parsed_tree[bag][v] = parsed_tree[v]

   return parsed_tree

def count_inner_tree(my_list):
   found_inner_shiny = False
   for key, values in my_list.items(): 
      if (key == 'shiny gold'): 
         found_inner_shiny = True
         break
      else:
         if (values == 'End'):
            continue
         else: 
            found_inner_shiny = count_inner_tree(values)
      if(found_inner_shiny):
         break
   return found_inner_shiny

def count_frequency(my_list): 
   count = 0
   for key, values in my_list.items(): 
      if (values == 'End'):
         continue
      else: 
         found_shiny = count_inner_tree(values)

      if(found_shiny):
         count += 1

   return count

regulations_tree = build_regulation_tree(baggage_regulations_raw)
parsed_tree = parse_regulations(regulations_tree)

def pretty_print(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty_print(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

# pretty_print(regulations_tree)
shiny_freq_count = count_frequency(parsed_tree)

print(f"Part 1 -- Bags that can contain a shiny gold: {shiny_freq_count}")