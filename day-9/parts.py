import json
from collections import defaultdict
from functools import cmp_to_key
from itertools import pairwise

sample = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]

def get_delta_history(values):
    delta_history = [values]
    while True:
        deltas = [b - a for a,b in pairwise(values)]
        delta_history.append(deltas)
        all_zeros = True
        for n in deltas:
            if n != 0:
                all_zeros = False
                break
        if all_zeros:
            break
        values = deltas
    return delta_history

def get_next_value(values):
    delta_history = get_delta_history(values)

    for idx, d in enumerate(reversed(delta_history[:-1])):
        d.append(d[-1] + delta_history[-idx-1][-1])

    return delta_history[0][-1]

def get_prev_value(values):
    delta_history = get_delta_history(values)

    for idx, d in enumerate(reversed(delta_history[:-1])):
        d.insert(0, d[0] - delta_history[-idx-1][0])

    print(delta_history)
    return delta_history[0][0]


def part_1(file_name):
    if not file_name:
        lines = sample
    else:
        lines = [l[:-1] for l in open(file_name, "r").readlines()]

    sum = 0
    for l in lines:
        if not l:
            continue
        values = [int(n) for n in l.split(' ')]
        next = get_next_value(values)
        sum += next
    print(sum)


def part_2(file_name):
    if not file_name:
        lines = sample
    else:
        lines = [l[:-1] for l in open(file_name, "r").readlines()]

    sum = 0
    for l in lines:
        if not l:
            continue
        values = [int(n) for n in l.split(' ')]
        next = get_prev_value(values)
        sum += next
    print(sum)

if __name__ == "__main__":
    #part_1(None)
    #part_1("input.txt")
    part_2(None)
    part_2("input.txt")
