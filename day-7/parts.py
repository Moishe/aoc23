import json
from collections import defaultdict
from functools import cmp_to_key

sample = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]
"""
char_to_score = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}
"""
char_to_score_part_2 = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def get_score_map(hand, char_to_score):
    hand_dict = defaultdict(int)
    for c in hand:
        hand_dict[c] += 1
    score_map = defaultdict(list)
    max_score_type = 0

    for v,k in hand_dict.items():
        score_map[k].append(char_to_score[v])

    if 5 in score_map:
        score_type = 7
    elif 4 in score_map:
        score_type = 6
    elif 3 in score_map:
        if 2 in score_map:
            score_type = 5
        else:
            score_type = 4
    elif 2 in score_map:
        if len(score_map[2]) == 2:
            score_type = 3
        else:
            score_type = 2
    else:
        score_type = 1

    score_array = [score_type]
    score_array.extend([char_to_score[c] for c in hand])
    return score_array

def part_1(file_name):
    if not file_name:
        lines = sample
    else:
        lines = [l[:-1] for l in open(file_name, "r").readlines()]

    scores = []
    for l in lines:
        hand, bid = l.split(" ")
        scores.append((int(bid), hand, get_score_map(hand)))
    print(scores)
    scores.sort(key=lambda x: x[2])
    sum = 0
    for idx, v in enumerate(scores):
        print(v, idx + 1)
        sum += v[0] * (idx + 1)
    print(json.dumps(scores, indent=2), sum)

def get_wildcard_hands(hand):
    hand_list = [hand]
    for idx, c in enumerate(hand):
        if c == 'J':
            for candidate_replacement in list(char_to_score_part_2.keys())[:-1]:
                new_hand = hand.copy()
                new_hand[idx] = candidate_replacement
                hand_list.extend(get_wildcard_hands(new_hand))

    return [''.join(x) for x in hand_list]

def part_2(use_sample):
    if use_sample:
        lines = sample
    else:
        lines = [l[:-1] for l in open("input.txt", "r").readlines()]

    scores = []
    for l in lines:
        hand, bid = l.split(" ")
        candidate_hands = get_wildcard_hands(list(hand))
        max_type = 0
        for candidate_hand in candidate_hands:
            candidate_score = get_score_map(candidate_hand, char_to_score_part_2)
            max_type = max(max_type, candidate_score[0])

        best_score = [max_type]
        best_score.extend([char_to_score_part_2[c] for c in hand])
        scores.append((int(bid), hand, best_score))

    scores.sort(key=lambda x: x[2])
    print(scores)
    sum = 0
    for idx, v in enumerate(scores):
        print(v, idx + 1)
        sum += v[0] * (idx + 1)
    print(sum)

if __name__ == "__main__":
    #part_1(None)
    #part_1("input.txt")

    part_2(False)
