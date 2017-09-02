"""
字符串全排列。
给定字符串S[0...N-1]，设计算法，枚举S的全排列。
"""


def permutation(l, length, n):
    """递归，重复"""
    if n == length - 1:
        print(l)
        return
    for i in range(n, length):
        l[i], l[n] = l[n], l[i]
        permutation(l, length, n + 1)
        l[i], l[n] = l[n], l[i]


def permutation2(l, length, n):
    """递归，去除重复"""
    if n == length - 1:
        print(l)
        return
    for i in range(n, length):
        if l[i] in l[n:i]:
            continue
        l[i], l[n] = l[n], l[i]
        permutation(l, length, n + 1)
        l[i], l[n] = l[n], l[i]


def permutation3(l, length, n):
    """递归，去除重复，并用空间换时间"""
    if n == length - 1:
        print(l)
        return

    dup = {}
    for i in range(n, length):
        if dup.setdefault(l[i], 0) == 1:
            continue
        dup[l[i]] = 1
        l[i], l[n] = l[n], l[i]
        permutation(l, length, n + 1)
        l[i], l[n] = l[n], l[i]


if __name__ == '__main__':
    l = [1, 2, 2]
    print('-----duplicate-----')
    permutation(l, len(l), 0)
    print('-----no duplicate-----')
    permutation2(l, len(l), 0)
    print('-----no duplicate, quicker-----')
    permutation3(l, len(l), 0)
