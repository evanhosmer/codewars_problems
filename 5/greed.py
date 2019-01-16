from collections import Counter
def score(dice):
    s = 0
    count = Counter(dice)
    if count[1] < 3:
        s += count[1] * 100
    if count[5] < 5:
        s += count[5] * 50
    scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    for key in count:
        if count[key] == 3:
            s += scores[key]
        if key == 1 and count[key] > 3:
            s += scores[key] + 100 * (count[key] - 3)
        if key == 5 and count[key] > 3:
            s += scores[key] + 50 * (count[key] - 3)

    return s


if __name__ == '__main__':
    '''
     5 1 3 4 1   50 + 2 * 100 = 250
     1 1 1 3 1   1000 + 100 = 1100
     2 4 4 5 4   400 + 50 = 450
    '''
    print(score([5,1,3,4,1]))
    print(score([1,1,1,3,1]))
    print(score([2,4,4,5,4]))
    print(score([3,3,3,4,4]))
