import itertools
from collections import defaultdict

sample = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

def part_1(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    seeds = [int(s) for s in lines[0].split(": ")[1].split(" ")]
    source, dest = (None, None)
    maps = defaultdict(lambda: defaultdict(list))

    for l in lines[1:]:
        if l == "":
            source, dest = (None, None)
            continue
        if "map:" in l:
            (source, dest) = l[:-5].split("-to-")
        else:
            (dest_no, source_no, r) = [int(x) for x in l.split(" ")]
            maps[source][dest].append((source_no, dest_no, r))

    s = 'seed'
    d = None
    values = seeds
    while d != 'location':
        new_values = []
        d = list(maps[s].keys())[0]
        for v in values:
            found = False
            for el in maps[s][d]:
                sval, dval, r = el
                if v in range(sval, sval + r):
                    new_values.append(dval + v - sval)
                    found = True
            if not found:
                new_values.append(v)
        values = new_values
        s = d

    print(min(values))

def overlap(start1, end1, start2, end2):
    if (end1 >= start2 and end2 >= start1):
        start = max(start1, start2)
        end = min(end1, end2)
        print(start, end)
        return (start, end)
    return None

def part_2(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    seeds = [int(s) for s in lines[0].split(": ")[1].split(" ")]
    seeds = list(itertools.pairwise(seeds))[::2]
    seeds = [(s[0], s[0] + s[1] - 1) for s in seeds]
    seeds = sorted(seeds, key=lambda x: x[0])

    source, dest = (None, None)
    maps = defaultdict(lambda: defaultdict(list))

    for l in lines[1:]:
        if l == "":
            source, dest = (None, None)
            continue
        if "map:" in l:
            (source, dest) = l[:-5].split("-to-")
        else:
            (dest_no, source_no, r) = [int(x) for x in l.split(" ")]
            source_start = source_no
            source_end = source_no + r - 1
            offset = dest_no - source_no
            maps[source][dest].append((source_start, source_end, offset))

    for source in maps:
        for dest in maps[source]:
            maps[source][dest].sort(key=lambda x: x[0])
            print(source, dest, maps[source][dest])

    s = 'seed'
    d = None
    values = seeds
    print(values)
    while d != 'location':
        new_values = []
        d = list(maps[s].keys())[0]
        print(s,d)
        for seed_start, seed_end in values:
            found = False
            for el in maps[s][d]:
                source_start, source_end, offset = el
                ov = overlap(seed_start, seed_end, source_start, source_end)
                if ov:
                    print(f"overlap: {seed_start}-{seed_end} {source_start}-{source_end} {ov}")
                    new_values.append((ov[0] + offset, ov[1] + offset))
                    found = True
            if not found:
                new_values.append((seed_start, seed_end))
        values = new_values
        print(values)
        s = d

    print(values)

if __name__ == "__main__":
    part_1(False)
    part_2(True)
