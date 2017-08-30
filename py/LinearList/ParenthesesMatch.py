"""
给定字符串，仅由“()[]{}”六个字符组成。设计算法，判断该字符串是否有效。
括号必须以正确的顺序配对，如：“()”、“{}[]” 是有效的，
但“([)]” 是无效的。
"""
parentheses_map = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def match_parentheses(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or parentheses_map[stack[-1]] != c:
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    s = '(({})[])[()]'
    print(s, match_parentheses(s))

    s = '(({})[)][()]'
    print(s, match_parentheses(s))
