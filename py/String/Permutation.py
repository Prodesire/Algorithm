"""
字符串全排列。
给定字符串S[0...N-1]，设计算法，枚举S的全排列。
"""


def permutation(l, length, n):
    if n == length - 1:
        print(l)
        return
    for i in range(n, length):
        l[i], l[n] = l[n], l[i]
        permutation(l, length, n + 1)
        l[i], l[n] = l[n], l[i]


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    permutation(l, len(l), 0)
