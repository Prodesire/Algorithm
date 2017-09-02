"""
找出给定数组最长且单调递增的子序列的长度。
如：
    给定数组[5,6,7,1,2,8]，则其最长单调递增子序列为[5,6,7,8]，长度为4
思路：
    其中一种方案就是拿排序后的数组和原数组做LCS，当然这不是最佳方案。
"""
from LCS import lcs


def lis(l):
    s1 = ''.join(str(i) for i in l)
    s2 = ''.join(sorted(s1))
    return lcs(s1, s2)


if __name__ == '__main__':
    l = [5, 6, 7, 1, 2, 8]
    print(l, lis(l))
