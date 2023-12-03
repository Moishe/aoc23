import re
from collections import defaultdict

sample = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def part_1(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    numbers = []
    symbols = set()
    for y, l in enumerate(lines):
        l.strip()
        for x, el in enumerate(l):
            if el != "." and not el.isdigit():
                for yy in (max(0, y - 1), y, min(y + 1, len(lines) - 1)):
                    for xx in (max(0, x - 1), x, min(x + 1, len(lines[yy]) - 1)):
                        if lines[yy][xx].isdigit():
                            # find the digits around the symbol
                            xxx = xx
                            n = ""
                            while xxx >= 0 and lines[yy][xxx].isdigit():
                                symbols.add(el)
                                n = lines[yy][xxx] + n
                                lines[yy] = (
                                    lines[yy][:xxx] + "." + lines[yy][xxx + 1 :]
                                )  # remove the digit
                                xxx -= 1

                            xxx = xx + 1
                            while xxx < len(l) and lines[yy][xxx].isdigit():
                                symbols.add(el)
                                n += lines[yy][xxx]
                                lines[yy] = lines[yy][:xxx] + "." + lines[yy][xxx + 1 :]
                                xxx += 1

                            numbers.append(n)

    ints = [int(x) for x in numbers]
    print(sum(ints))


def part_2(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    numbers = []
    symbols = set()
    for y, l in enumerate(lines):
        l.strip()
        for x, el in enumerate(l):
            if el == "*":
                operands = []
                for yy in (max(0, y - 1), y, min(y + 1, len(lines) - 1)):
                    for xx in (max(0, x - 1), x, min(x + 1, len(lines[yy]) - 1)):
                        if lines[yy][xx].isdigit():
                            # find the digits around the symbol
                            xxx = xx
                            n = ""
                            while xxx >= 0 and lines[yy][xxx].isdigit():
                                symbols.add(el)
                                n = lines[yy][xxx] + n
                                lines[yy] = (
                                    lines[yy][:xxx] + "." + lines[yy][xxx + 1 :]
                                )  # remove the digit
                                xxx -= 1

                            xxx = xx + 1
                            while xxx < len(l) and lines[yy][xxx].isdigit():
                                symbols.add(el)
                                n += lines[yy][xxx]
                                lines[yy] = lines[yy][:xxx] + "." + lines[yy][xxx + 1 :]
                                xxx += 1

                            operands.append(n)
                if len(operands) == 2:
                    numbers.append(int(operands[0]) * int(operands[1]))

    print(sum(numbers))

if __name__ == "__main__":
    part_1(False)
    part_2(False)
