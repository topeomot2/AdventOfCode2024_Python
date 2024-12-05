import re

def match_multiplications(content):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    return re.findall(pattern, content)

def multiplications1():
    with open("input.txt", "r") as file:
        content = file.read()


    matches = match_multiplications(content)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])

    return total


def multiplications2():
    with open("input.txt", "r") as file:
        content = file.read()

    total = 0

    pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
    instructions = re.findall(pattern, content)

    can_use = True
    for instruction in instructions:
        if instruction == "don't()":
            can_use = False
            continue

        if instruction == "do()":
            can_use = True
            continue

        if can_use:
            match = match_multiplications(instruction)
            total += int(match[0][0]) * int(match[0][1])

    return total







# Find and print matches
print(multiplications1())
print(multiplications2())