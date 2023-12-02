import re
from collections import defaultdict
from functools import reduce

sample = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def part_1(use_sample):
    if use_sample:
        games = sample
    else:
        games = open("input.txt", "r")

    sum = 0
    for g in games:
        g = g.strip()
        (_, cubes) = g.split(": ")
        subgames = cubes.split("; ")
        colors = defaultdict(int)
        for subgame in subgames:
            subcubes = subgame.split(", ")
            for cube in subcubes:
                (count, color) = cube.split(" ")
                colors[color] = max(colors[color], int(count))
        power = reduce(lambda x, y: x * y, colors.values())
        sum += power
    print(sum)

if __name__=="__main__":
    part_1(False)
