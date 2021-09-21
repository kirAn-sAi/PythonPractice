# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def do_magic(cube):
    # write your code in Python 3.6
    totals = []
    for i in range(3):
        row = (cube[i * 3], cube[i * 3 + 1], cube[i * 3 + 2])
        col = (cube[i], cube[i + 3], cube[i + 6])

        data = (sum(row), sum(col))
        totals.append(data)

    target = max(max(totals))

    sibling_map = {
        0: ((0, 1, 2), (0, 3, 6)),
        1: ((0, 1, 2), (1, 4, 7)),
        2: ((0, 1, 2), (2, 5, 8)),
        3: ((3, 4, 5), (0, 3, 6)),
        4: ((3, 4, 5), (1, 4, 7)),
        5: ((3, 4, 5), (2, 5, 8)),
        6: ((6, 7, 8), (0, 3, 6)),
        7: ((6, 7, 8), (1, 4, 7)),
        8: ((6, 7, 8), (2, 5, 8)),
    }
    get_total = lambda vals: sum((cube[vals[0]], cube[vals[1]], cube[vals[2]]))
    # get_substitute = lambda x: sum(cube[])
    print(cube)
    print(target)

    for i in range(9):
        ct = get_total(sibling_map[i][0])
        rt = get_total(sibling_map[i][1])
        print(ct, rt)
        if rt != target and ct != target:
            # print(i, cube[i], target, ct)
            cube[i] += target - ct
    return cube



inputs = (
    # [0, 2, 3, 4, 1, 1, 1, 3, 1],
    # [1, 1, 1, 2, 2, 1, 2, 2, 1],
    # [35000, 35000, 25000, 35000, 25000, 35000, 25000, 35000, 25000],
    # [2000000, 3000000, 3000000, 3000000, 2000000, 3000000, 2000000, 3000000, 2000000],
    [3, 2, 0, 0, 0, 0, 0, 3, 2],
)

for ip in inputs:
    print(do_magic(ip))
