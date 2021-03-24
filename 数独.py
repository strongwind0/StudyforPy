import time


def list2set(data):
    '''列表->集合九宫格'''
    L = [[set(range(1, 10)) for i in range(9)] for j in range(9)]
    for i in range(9):
        for j in range(9):
            if data[i][j]:
                L[i][j] = {data[i][j]}
    return L


def sudoku_filter(L, i, j):
    a = list(L[i][j])[-1]
    for k in range(9):
        if k != i and a in L[k][j]:
            L[k][j].remove(a)
        if k != j and a in L[i][k]:
            L[i][k].remove(a)
    m, n = (i // 3, j // 3)
    for u in range(3):
        for v in range(3):
            if (u, v) != (i % 3, j % 3) and a in L[3 * m + u][3 * n + v]:
                L[3 * m + u][3 * n + v].remove(a)


def sudoku_puzzle(L, out=False, solve=False):
    from copy import deepcopy
    if isinstance(out, bool):
        out = []
    if isinstance(solve, bool):
        solve = set()
    if not isinstance(L[0][0], set):
        L = list2set(L)
    while True:
        flag = False
        for i in range(9):
            for j in range(9):
                if (i, j) in solve:
                    continue
                if len(L[i][j]) == 1:
                    sudoku_filter(L, i, j)
                    solve.add((i, j))
                    flag = True
        if not flag:
            break
    if len(solve) == 81:
        out.append([[j.pop() for j in i] for i in L])
        return out
    m = 9
    for i in range(9):
        for j in range(9):
            if (i, j) not in solve and len(L[i][j]) <= m:
                m = len(L[i][j])
                small = (i, j)
    if m == 0:
        return out
    i, j = small
    for k in L[i][j]:
        solve2, L2, L2[i][j] = solve.copy(), deepcopy(L), {k}
        sudoku_puzzle(L2, out, solve2)
    return out


str2list = lambda s: [[int(s[9 * j + i]) for i in range(9)] for j in range(9)]
if __name__ == '__main__':
    while True:
        print("请按照从左至右，从上至下的顺序输入，空位用0替换")
        s = input("输入数据：")
        t = time.time()
        if len(s) != 81:
            print("输入的数独字符串长度错误,请重新输入")
        else:
            l = str2list(s)
            for row in l:
                print(row)
            out = sudoku_puzzle(l)
            print('计算用时:{:.3f}'.format(time.time() - t))
            print('总解数：', len(out))
            for data in out:
                for row in data:
                    print(row)
                print()
        if input("按Enter继续，按0+Enter退出") == '0':
            break
