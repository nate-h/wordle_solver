import json
from collections import Counter
from typing import Iterator, List, Set


# Load 5 letter words.
with open("data/all_words.json") as json_file:
    all_words = json.load(json_file)
with open("data/valid_five_letter_words.json") as json_file:
    all_words += json.load(json_file)
words = all_words.copy()
dupeless_all_words = ["".join(set(w)) for w in words]


def char_count(remove_chars: str=""):
    """Count occurrence of each character and remove chars from counts."""
    dupeless_words = ["".join(set(w)) for w in words]
    counts = Counter("".join(dupeless_words))
    for c in remove_chars:
        del counts[c]
    return counts


def explore(contains:str):
    """Find words in this list that contain all letters in 'contains'."""
    return [w for w in all_words if all(c in w for c in contains)]


def find(remove_chars: str, top=1) -> str:
    """Given a list of possible words left, find the optimal word to
    guess next.
    """
    # Count occurrence of each char for remaining words.
    counts = char_count(remove_chars)

    # Find word in all words that maximizes count of highest occurring chars.
    scores = [sum(map(lambda c: counts[c], w)) for w in dupeless_all_words]

    # Return word(s) with max score.
    return sorted(list(zip(all_words, scores)), key=lambda x: x[1], reverse=True)[:top]


def update(guess: str, outcome: str) -> Iterator[str]:
    """Filters a list of words give a guess and it's outcome in wordle.

    Parameters:
        words: the list of words to filter
        guess: your wordle guess
        outcome: a string representing how close the guess matches to the word.
            letters not in the final word are marked with `_`
            letters in the correct position are marked with a capital letter
            letters in the incorrect position are marked with a lowercase letter
    """

    is_out: Set[str] = set()
    constraints = set() # is_at_index, index, char

    for i, (g, o) in enumerate(zip(guess, outcome)):
        if o == '_':
            is_out.add(g)
        elif o.isupper():
            constraints.add((True, i, g))
        else:
            constraints.add((False, i, g))

    ret_words = []
    for w in words:
        # Exclude words.
        if is_out.intersection(w):
            continue
        # Test if letters are at or not at a certain index.
        do_add = True
        for is_at_index, index, char in constraints:
            if is_at_index:
                if w[index] != char:
                    do_add = False
                    break
            else:
                if w[index] == char:
                    do_add = False
                    break
                if char not in w:
                    do_add = False
                    break

        if do_add:
            ret_words.append(w)

    return ret_words
