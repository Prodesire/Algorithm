"""
给定两个链表，分表表示两个非负整数。它们的数字逆序储存在链表中，
且每个节点只储存一个数字，计算两个数的和，并且返回和的链表头指针。
如：
    输入： 2->4->3, 5->6->4
    输出： 7->0->8
"""
from Base import Node, gen_linkedlist


def add(phead1, phead2):
    psum = Node(0)
    ptail = psum
    p1 = phead1.next
    p2 = phead2.next
    carry = 0

    while p1 and p2:
        value = p1.value + p2.value + carry
        carry = value // 10
        value %= 10
        ptail.next = Node(value)
        ptail = ptail.next

        p1 = p1.next
        p2 = p2.next

    p = p1 if p1 else p2
    while p:
        value = p.value + carry
        carry = value // 10
        ptail.next = Node(value)
        ptail = ptail.next
        p = p.next

    if carry:
        ptail.next = Node(carry)
    return psum


if __name__ == '__main__':
    phead1 = gen_linkedlist(6)
    phead2 = gen_linkedlist(9)

    print(phead1)
    print(phead2)
    psum = add(phead1, phead2)
    print(psum)
