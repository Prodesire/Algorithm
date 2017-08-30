"""
给定无重复元素的两个等长数组，分别表示入栈序列和出栈序列。
请问：这样的出栈序列是否可行。
如：
    入栈序列为 “ABCDEFG”，出栈序列为 “BAEDFGC”，则可行。
    入栈序列为 “ABCD”，出栈序列为 “BDAC”，则可行。
"""


def stack_inout_possible(in_seq, out_seq):
    stack = []
    i = j = 0

    while j < len(out_seq):
        if stack and out_seq[j] == stack[-1]:
            stack.pop()
            j += 1
        else:
            if i == len(in_seq):
                return False
            stack.append(in_seq[i])
            i += 1

    return not stack


if __name__ == '__main__':
    print(stack_inout_possible('ABCDEFG', 'BAEDFGC'))
    print(stack_inout_possible('ABCD', 'BDAC'))
