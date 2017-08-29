"""
给定一个链表，翻转该链表从 m 到 n 的位置。
要求直接翻转而非申请空间。
如：
    输入： 1->2->3->4->5, m=2, n=4
    输出： 1->4->3->2->5
"""
from random import randint
from Structure import Node


def reverse(phead, m, n):
    pcur = phead
    for i in range(0, m-1):
        pcur = pcur.next

    ppre = pcur
    pcur = pcur.next

    for i in range(m, n):
        pnext = pcur.next
        pcur.next = pnext.next
        pnext.next = ppre.next
        ppre.next = pnext


if __name__ == '__main__':
    phead = Node(0)
    for i in range(10):
        p = Node(randint(0, 9))
        p.next = phead.next
        phead.next = p

    print(phead)
    reverse(phead, 4, 8)
    print(phead)
