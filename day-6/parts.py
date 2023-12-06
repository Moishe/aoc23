import re
from collections import defaultdict
from functools import reduce

sample = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def part_1(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    times = [int(s) for s in re.findall(r"(\d+)", lines[0])]
    distances = [int(s) for s in re.findall(r"(\d+)", lines[1])]

    all_wins = 1
    for race in zip(times,distances):
        t, d = race
        wins = 0
        for hold in range(0, t):
            candidate = hold * (t - hold)
            if candidate > d:
                wins += 1
        all_wins *= wins

    print(all_wins)


def part_2(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    time = int(''.join(re.findall(r"(\d+)", lines[0])))
    distance = int(''.join(re.findall(r"(\d+)", lines[1])))

    wins = 0
    for hold in range(0, time):
        candidate = hold * (time - hold)
        if candidate > distance:
            wins += 1

    print(wins)


if __name__ == "__main__":
    part_1(False)
    part_2(False)
