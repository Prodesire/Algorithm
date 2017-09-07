"""
给定字符串 s, 若子串 ss 是回文串，称 ss 为 s 的回文串。
设计算法，计算 s 的最长回文串。
"""


def manacher(s):
    length = len(s)
    P = [0] * length
    P[0] = 1
    id = 1
    mx = 1
    for i in range(1, length):
        if mx > i:
            P[i] = min(P[2*id-i], mx-i)
        else:
            P[i] = 1
        
        while s[i+P[i]] != s[i-P[i]]:
            print(i, i+P[i], i-P[i])
            P[i] += 1

        if mx < i + P[i]:
            mx = i + P[i]
            id = i
    print(P)


if __name__ == '__main__':
    s = 'abbbabbb'
    manacher(s)
