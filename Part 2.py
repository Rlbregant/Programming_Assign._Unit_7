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


def missing_letters(s):
    hist = histogram(s)
    missing = ""
    for letter in alphabet:
        if letter not in hist:
            missing += letter
    if missing == "":
        return s + " uses all the letters"
    else:
        return s + " is missing letters " + missing


def main():
    for s in test_miss:
        print(missing_letters(s))


if __name__ == '__main__':
    main()

# Output:
# zzz is missing letters abcdefghijklmnopqrstuvwxy
# subdermatoglyphic uses all the letters
# the quick brown fox jumps over the lazy dog is missing letters c
