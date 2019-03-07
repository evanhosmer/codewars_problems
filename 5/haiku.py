import re
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def is_haiku(poem):
    if poem == '':
        return False
    poem = poem.lower()
    lines = poem.split('\n')
    vowels = "aeiouy"
    counts = []
    for line in lines:
        syll = 0
        for word in line.split(' '):
            if any(c.isalpha() for c in word):
                syll += syllable_count(word)
            else:
                continue
        counts.append(syll)

    print(counts)

    if counts == [5,7,5]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_haiku("""\
An old silent pond...
A frog jumps into the pond,
splash! Silence again."""))

    print(is_haiku("""\
Aid fighting sir roof...
Scale make like increase get pole
Proposed soil nerve?"""))
