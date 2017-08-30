"""
给定字符串，仅包含左括号“(”和右括号“)”，它可能不是括号匹配的。
设计算法，找出最长匹配的括号子串，返回该子串的长度。
如：
    ((): 2
    ()(): 4
    ()(()): 6
    (()()): 6
"""


def match_parentheses_maxlength(s):
    maxlength = 0
    start = -1
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if not stack:
                start = i
            else:
                stack.pop()
                if not stack:
                    maxlength = max(maxlength, i - start)
                else:
                    maxlength = max(maxlength, i - stack[-1])
    return maxlength


def match_parentheses_maxlength2(s):
    maxlength = 0

    def traverse(string, parenthese):
        nonlocal maxlength
        start = -1
        deep = 0
        for i, c in enumerate(string):
            if c == parenthese:
                deep += 1
            else:
                deep -= 1
                if deep == 0:
                    maxlength = max(maxlength, i - start)
                elif deep < 0:
                    deep = 0
                    start = i
    traverse(s, '(')
    traverse(reversed(s), ')')
    return maxlength


if __name__ == '__main__':
    for s in ['(()', '()()', '()(())', '(()())', '(()()))']:
        print(s, match_parentheses_maxlength(s))
        print(s, match_parentheses_maxlength2(s))
