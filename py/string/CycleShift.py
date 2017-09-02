"""
给定一个字符串S[0...N-1]，要求把S的前k个字符移动到S的尾部。
要求时间复杂度为O(n)，空间复杂度为O(1)。
如：
    把字符串'abcdef'前两个字符'a'、'b'移动到字符串尾部得到'cdefab'
思路：
    根据数学原理 (A'B')' = BA，就是先转置A，再转置B，再转置A'B'，就能得到BA
"""


def cycle_shift(s, n, k):
    k %= n
    reverse(s, 0, k - 1)
    reverse(s, k, n - 1)
    reverse(s, 0, n - 1)


def reverse(s, from_, to):
    while from_ < to:
        s[from_], s[to] = s[to], s[from_]
        from_ += 1
        to -= 1


if __name__ == '__main__':
    s = list('abcdef')
    print(s)
    cycle_shift(s, len(s), 2)
    print(s)
