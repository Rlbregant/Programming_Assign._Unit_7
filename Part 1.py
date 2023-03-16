alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def has_duplicates(s):
    hist = histogram(s)
    for val in hist.values():
        if val > 1:
            return True
    return False


def main():
    for s in test_dups:
        if has_duplicates(s):
            print(s, "has duplicates")
        else:
            print(s, "has no duplicates")


if __name__ == '__main__':
    main()

# Output:
# zzz has duplicates
# dog has no duplicates
# bookkeeper has duplicates
# subdermatoglyphic has no duplicates
# subdermatoglyphics has duplicates
