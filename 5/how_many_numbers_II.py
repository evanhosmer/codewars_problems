import numpy as np

def max_sumDig(nmax, maxs):
    l = list(range(1000, nmax + 1))
    results = []
    for n in l:
        if sum(int(digit) for digit in str(n)) <= maxs:
            results.append(n)

    m = np.mean(results)
    two = min(results, key=lambda x:abs(x-m))

    return [len(results), two, sum(results)]

if __name__ == '__main__':
    print(max_sumDig(3000, 7))
