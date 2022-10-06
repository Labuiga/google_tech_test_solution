# coding: utf-8
# author: David Labuiga
from json import loads
from argparse import ArgumentParser


def solve(a, b, n, ac):
    """Strategy:
        1- union set with the purpose of minimizing the number of groups that will be evaluated
        2 - efficiently combine for the case"""
    # union
    a = set(a)
    b = set(b)
    u = [e for e in a.union(b) if e <= n]
    g = [e for e in u if n - max(u) < e]
    # combinatorics
    x1, y1 = -1, -1
    r = []
    while g:
        x = g.pop(0) if x1 < 0 else x1
        y = g.pop(len(g) - 1) if y1 < 0 else y1
        d = x + y
        if d > n:
            x1 = x
        elif d < n:
            y1 = y
        else:
            r.append((x, y))
            x1, y1 = -1, -1

    return r


def main(config):
    if config:
        a, b, n, ac = loads(open('config.json', 'r').read()).values()
    else:
        a = [1, 3, 5, 6, 9]
        b = [0, 1, 2, 4, 8]
        n = 8
        ac = 1  # allow combinations of the same group
    solve(a, b, n, ac)


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-c', '--config', help='allow config json', type=bool, default=False)
    args = vars(ap.parse_args())
    main(config=args['config'])
