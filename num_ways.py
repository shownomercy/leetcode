"""
given a ladder with n levels, and a array of steps that are available to take,
return the possible ways that ladder can be climbbed
"""


def num_ways(n, steps):
    results = []
    results.append(1)
    if (n == 0):
        return 1
    for ladder in range(1, n + 1):
        result = 0
        for s in steps:
            if (ladder - s >= 0):
                result += results[ladder - s]

        results.append(result)
    return results[n]


print(num_ways(100, [1, 100]))
