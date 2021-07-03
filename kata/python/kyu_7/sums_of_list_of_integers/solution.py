import itertools

def equals_sum(num_arr, total):
    res = []
    for i in range(1, len(num_arr) + 1):
        for c in itertools.combinations(num_arr, i):
            if sum(c) == total:
                res.append(list(c))
                res[-1].sort()
    res = list(k for k,_ in itertools.groupby(res))
    return res