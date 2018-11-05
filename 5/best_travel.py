from itertools import combinations
import bisect
def choose_best_sum(t, k, ls):
    combs = [comb for comb in combinations(ls,k)]
    sums = list(map(sum,combs))
    sums.sort()
    if all(i > t for i in sums):
        return None
    ind = bisect.bisect(sums,t,lo = 0, hi = len(sums))
    return max(sums[0:ind])

if __name__ == '__main__':
    t = 230
    k = 3
    ls = [91, 74, 73, 85, 73, 81, 87]
    print(choose_best_sum(t,k,ls))
