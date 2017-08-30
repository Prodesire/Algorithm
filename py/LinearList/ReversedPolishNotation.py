"""
计算给定的逆波兰表达式的值。有效操作只有 +-*/ ，每个操作数都是整数。
如：
    "2", "1", "+", "3", "*" -> (2+1)*3 -> 9
    "4", "13", "5", "/", "+" -> 4+(13/5) -> 6.6
"""


def reversed_polish(notation):
    stack = []
    for token in notation:
        if token not in '+-*/':
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            value = eval('{}{}{}'.format(a, token, b))
            stack.append(value)
    return stack.pop()


if __name__ == '__main__':
    for notation in [["2", "1", "+", "3", "*"],
                     ["4", "13", "5", "/", "+"]]:
        print(notation, reversed_polish(notation))
