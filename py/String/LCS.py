"""
求两个字符串的最长公共子序列的长度。
如：
    字符串'abcbdab'和'bdcaba'的LCS长度是4。
"""


def lcs(s1, s2):
    len1 = len(s1) + 1
    len2 = len(s2) + 1
    c = [[0 for _ in range(len2)] for _ in range(len1)]
    for i in range(1, len1):
        for j in range(1, len2):
            if s1[i - 1] == s2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[len1 - 1][len2 - 1]


if __name__ == '__main__':
    s1 = 'abcbdab'
    s2 = 'bdcaba'
    print(s1, s2, lcs(s1, s2))
