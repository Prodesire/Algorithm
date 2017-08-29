"""
给定排序的链表，删除重复元素，只保留重复元素第一次出现的节点。
如：
    输入： 2->3->3->5->7->8->8->9->9->10
    输出： 2->3->5->7->8->9->10
"""
from Base import gen_linkedlist


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
    phead = gen_linkedlist(20)

    print(phead)
    uniq(phead)
    print(phead)
