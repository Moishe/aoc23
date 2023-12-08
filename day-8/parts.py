import re
import json
from collections import defaultdict
from functools import reduce

sample = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

sample_2 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]

def get_path_and_map(lines):
    path = lines[0]
    map = {}
    for l in lines[2:]:
        key = l.split(" = ")[0]
        values = l.split(" = ")[1][1:-1].split(", ")
        map[key] = {
            "L": values[0],
            "R": values[1],
        }

    return path, map

def part_1(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    path, map = get_path_and_map(lines)

    steps = 0
    loc = "AAA"
    while True:
        for p in path:
            steps += 1
            loc = map[loc][p]
            if loc == 'ZZZ':
                print(f"Found in {steps} steps")
                return


def part_2(use_sample):
    if use_sample:
        lines = sample_2
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    path, map = get_path_and_map(lines)

    steps = 0
    locs = list(filter(lambda x: x[2] == 'A', map))
    mx = 0
    counts_to_first_z = [0] * len(locs)
    while True:
        for f in path:
            steps += 1
            locs = [map[n][f] for n in locs]
            zs = [x[2] == 'Z' for x in locs]
            for idx, el in enumerate(zip(counts_to_first_z, zs)):
                cur_step, is_z = el
                if cur_step == 0 and is_z:
                    print(locs, steps, idx, counts_to_first_z)
                    counts_to_first_z[idx] = steps / len(path)

            if len(list(filter(lambda x: x == 0, counts_to_first_z))) == 0:
                print(counts_to_first_z)
                z = reduce(lambda x, y: x * y, counts_to_first_z)
                print(z * len(path), locs)
                return

if __name__ == "__main__":
    #part_1(False)
    part_2(True)
    part_2(False)
