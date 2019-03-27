from collections import Counter
'''
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or
None -- see sample tests.

'''

def first_non_repeating_letter(s):
    news = s.lower()
    counts = Counter(news)
    if all(value > 1 for value in counts.values()):
        return 'None'

    if len(counts) == 1:
        return s

    nonrepeat = [key for key in counts.keys() if counts[key] == 1]
    locs = []
    for letter in nonrepeat:
        ind = news.find(letter)
        locs.append((letter,ind))

    if not s.islower():
        return s[min(locs, key = lambda t: t[1])[1]]
    else:
        return min(locs, key = lambda t: t[1])[0]

if __name__ == '__main__':
    print(first_non_repeating_letter("stress"))
    print(first_non_repeating_letter('football'))
    print(first_non_repeating_letter('sTreSS'))
