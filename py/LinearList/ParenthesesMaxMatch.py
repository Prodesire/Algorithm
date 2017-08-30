"""
给定字符串，仅包含左括号“(”和右括号“)”，它可能不是括号匹配的。
设计算法，找出最长匹配的括号子串，返回该子串的长度。
如：
    ((): 2
    ()(): 4
    ()(()): 6
    (()()): 6
"""


def match_maxlength_parentheses(s):
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


if __name__ == '__main__':
    for s in ['(()', '()()', '()(())', '(()())', '(()()))']:
        print(s, match_maxlength_parentheses(s))
