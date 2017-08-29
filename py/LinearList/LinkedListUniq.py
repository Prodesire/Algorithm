"""
给定排序的链表，删除重复元素，只保留重复元素第一次出现的节点。
如：
    输入： 2->3->3->5->7->8->8->9->9->10
    输出： 2->3->5->7->8->9->10
"""
from random import randint
from Structure import Node


def uniq(phead):
    pcur = phead.next
    while pcur:
        pnext = pcur.next
        if not pnext:
            return
        if pcur.value == pnext.value:
            pcur.next = pnext.next
        pcur = pcur.next


if __name__ == '__main__':
    phead = Node(0)
    for i in range(10):
        p = Node(randint(0, 99) % 10)
        p.next = phead.next
        phead.next = p

    print(phead)
    uniq(phead)
    print(phead)
