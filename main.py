# coding: utf-8
# author: David Labuiga
from json import loads
from argparse import ArgumentParser

A = [1, 3, 5, 6, 9]  # array1
B = [0, 1, 2, 4, 8]  # array2
N = 8  # target sum
AC = 1  # allow combinations of the same array


def solve(a, b, n, ac):
    """Strategy:
        1 - union set with the purpose of sort and minimizing the number of groups that will be evaluated
        2 - efficiently combine for the case"""
    # union
    a = set(a)
    b = set(b)
    u = [e for e in a.union(b) if e <= n]
    g = [e for e in u if n - max(u) <= e]
    # if not ac:  # alternative way to evade so much if else - not inplemented
    #     a = [e for e in a if n - max(a) <= e <= n]
    #     b = [e for e in a if n - max(a) <= e <= n]
    # combinatorics
    x1, y1 = -1, -1
    r = []
    while g:
        x = g.pop(0) if x1 < 0 and g else x1
        y = g.pop(len(g) - 1) if y1 < 0 and g else y1 if y1 > 0 else x if x in a and x in b else -1
        if x >= 0 and y >= 0:
            d = x + y
            if d > n:
                x1 = x
                y1 = -1
            elif d < n:
                x1 = -1
                y1 = y
            else:
                if not ac:
                    if (x in a and y in b) or (y in a and x in b):
                        r.append((x, y))
                        x1, y1 = -1, -1
                    else:
                        x1 = x
                else:
                    r.append((x, y))
                    x1, y1 = -1, -1

    print(r)


def main(file, a, b, n, ac):
    if file:
        groups = loads(open('file.json', 'r').read())['groups']
        for g in groups:
            a, b, n, ac = g.values()
            solve(a, b, n, ac)
    else:
        if not a and b and n:
            a = A
            b = B
            n = N
            ac = AC
        solve(a, b, n, ac)


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-f', '--file', help='allow file json', type=bool, default=False)
    ap.add_argument('-a', '--array1', help='array1', type=list, default=A)
    ap.add_argument('-b', '--array2', help='array2', type=list, default=B)
    ap.add_argument('-n', '--number', help='target sum', type=bool, default=N)
    ap.add_argument('-ac', '--allow_combinations', help='allow combinations of the same array', type=bool, default=AC)
    args = vars(ap.parse_args())
    main(file=args['file'], a=args['array1'], b=args['array2'], n=args['number'], ac=args['allow_combinations'])
