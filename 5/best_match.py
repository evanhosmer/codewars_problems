from collections import Counter
def best_match(goals1, goals2):
    res = [a_i - b_i for a_i, b_i in zip(goals1, goals2)]
    tups = []
    for idx, val in enumerate(goals2):
        tups.append((val,res[idx]))

    lowval = min(tups, key = lambda t: t[1])[1]
    tups2 = [t for t in tups if t[1] == lowval]
    if Counter([y for (x,y) in tups])[lowval] > 1:
        val = max(tups2, key = lambda t: t[0])[0]
        return tups.index((val,lowval))
    else:
        return[y[1] for y in tups].index(lowval)



if __name__ == '__main__':
    print(best_match([6,4],[1,2]))
    print(best_match([1,2,3,4,5],[0,1,2,3,4]))
    print(best_match([4,3,4],[1,1,1]))
