from collections import Counter
def scramble(s1, s2):
    one = Counter(s1)
    two = Counter(s2)
    return all(two[i] <= one[i] for i in two)


if __name__ == '__main__':
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
    print(scramble('katas', 'steak'))
    print(scramble('scriptjava', 'javascript'))
    print(scramble('scriptingjava', 'javascript'))
