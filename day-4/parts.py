import re
from collections import defaultdict

sample = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def part_1(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    score = 0
    for l in lines:
        l.strip()
        (card, numbers) = l.split(": ")
        (winning, yours) = numbers.split(" | ")
        winning = set([int(n) for n in re.findall(r"\d+", winning)])
        yours = set([int(n) for n in re.findall(r"\d+", yours)])
        overlap = list(winning.intersection(yours))
        if len(overlap):
            score += 2 ** (len(overlap) - 1)

    print(score)


def part_2(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    multipliers = {i + 1:1 for i in range(len(lines))}
    print(len(multipliers))
    for l in lines:
        l.strip()
        (card, numbers) = l.split(": ")
        cardno = int(re.findall(r"\d+", card)[0])
        (winning, yours) = numbers.split(" | ")
        winning = set([int(n) for n in re.findall(r"\d+", winning)])
        yours = set([int(n) for n in re.findall(r"\d+", yours)])
        overlap = list(winning.intersection(yours))
        if len(overlap):
            print(f"{cardno}: Found {len(overlap)} overlaps, adding {len(overlap)} overlaps in {len(multipliers)} total items")
            for idx in range(0, len(overlap)):
                #print(idx)
                multipliers[cardno + idx + 1] += multipliers[cardno]
            #print(multipliers)

        #print(cardno, multipliers)

    print(sum(multipliers.values()))


if __name__ == "__main__":
    part_1(False)
    part_2(False)
