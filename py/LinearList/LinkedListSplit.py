"""
给定一个链表和一个值x，将链表划分成两部分，使得划分后小于x的节点在前，
大于等于x的节点在后。在这两部分中要保持原链表中的出现顺序。
如：
    输入： 1->4->3->2->5->2 和 x=3
    输出： 1->2->2->4->3->5
"""
from Base import Node, gen_linkedlist


def split(phead, x):
    pcur1 = p1 = Node(0)
    pcur2 = p2 = Node(0)
    pcur = phead.next

    while pcur:
        if pcur.value < x:
            pcur1.next = pcur
            pcur1 = pcur
        else:
            pcur2.next = pcur
            pcur2 = pcur
        pcur = pcur.next

    pcur1.next = p2.next
    pcur2.next = None
    phead.next = p1.next


if __name__ == '__main__':
    phead = gen_linkedlist(10)

    print(phead)
    split(phead, 5)
    print(phead)
