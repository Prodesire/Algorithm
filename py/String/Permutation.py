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
        permutation2(l, length, n + 1)
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
        permutation3(l, length, n + 1)
        l[i], l[n] = l[n], l[i]


def permutation4(l, length):
    """非递归，后找、小大、交换、翻转"""
    print(l)
    def get_next_permutation():
        # 后找
        i = length - 2
        while(i >= 0 and l[i] >= l[i+1]):
            i -= 1
        if i < 0:
            return False

        # 小大
        j = length - 1
        while(l[j] <= l[i]):
            j -= 1

        l[i], l[j] = l[j], l[i]
        l[i+1:length] = l[length-1:i:-1]
        return True
    
    while get_next_permutation():
        print(l)

if __name__ == '__main__':
    l = [1, 2, 2]
    print('-----duplicate-----')
    permutation(l, len(l), 0)
    print('-----no duplicate-----')
    permutation2(l, len(l), 0)
    print('-----no duplicate, quicker-----')
    permutation3(l, len(l), 0)
    print('-----no duplicate, no recursive-----')
    permutation4(l, len(l))