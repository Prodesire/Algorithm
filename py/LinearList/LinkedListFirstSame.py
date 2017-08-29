"""
给定两个单项链表，计算两个链表的第一个公共节点。
若没有，返回空。
"""

from Base import gen_linkedlist


def first_same(phead1, phead2):
    pcur1 = phead1.next
    pcur2 = phead2.next

    length1 = len(pcur1)
    length2 = len(pcur2)

    if length1 < length2:
        pcur1, pcur2 = pcur2, pcur1

    for i in range(abs(length1 - length2)):
        pcur1 = pcur1.next

    while pcur1:
        if pcur1 == pcur2:
            return pcur1
        pcur1 = pcur1.next
        pcur2 = pcur2.next


if __name__ == '__main__':
    pcommon = gen_linkedlist(2)
    phead1, tail1 = gen_linkedlist(2, with_tail=True)
    phead2, tail2 = gen_linkedlist(3, with_tail=True)
    tail1.next = pcommon.next
    tail2.next = pcommon.next
    print(phead1, phead2)
    print(first_same(phead1, phead2))
