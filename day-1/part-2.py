import re

numbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

def to_int(s):
    if s.isdigit():
        return int(s)
    else:
        return numbers.index(s) + 1

def part1():
    f = open("/Users/moishe/src/aoc-23/day-1/input.txt", "r")
    p = 0
    matches = ["[0-9]"]
    matches.extend(numbers)
    reverse_matches = ["[0-9]"]
    reverse_matches.extend([x[::-1] for x in numbers])

    first_regex = '|'.join(matches)
    last_regex = '|'.join(reverse_matches)

    for l in f:
        first_digit = re.findall(first_regex, l)[0]
        last_digit = re.findall(last_regex, l[::-1])[0]
        print(first_digit, last_digit)

        s = to_int(first_digit) * 10 + to_int(last_digit[::-1])
        print(f"{l.strip()}: {s}")
        p += s
    print(p)

if __name__ == "__main__":
    part1()
