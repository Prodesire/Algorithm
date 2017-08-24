"""
给定两个链表，分表表示两个非负整数。它们的数字逆序储存在链表中，
且每个节点只储存一个数字，计算两个数的和，并且返回和的链表头指针。
如：
    输入： 2->4->3, 5->6->4
    输出： 7->0->8
"""
from random import randint


class SNode(object):
    def __init__(self, value):
        self.value = int(value)
        self.next = None
    
    def __str__(self):
        p = self.next
        if not p:
            return ''

        output = str(p.value)
        while p.next:
            output += '->{}'.format(p.next.value)
            p = p.next
        return output


def add(phead1, phead2):
    psum = SNode(0);
    ptail = psum
    p1 = phead1.next
    p2 = phead2.next
    carry = 0

    while(p1 and p2):
        value = p1.value + p2.value + carry
        carry = value / 10
        value %= 10
        ptail.next = SNode(value)
        ptail = ptail.next

        p1 = p1.next
        p2 = p2.next
    
    p = p1 if p1 else p2
    while p:
        value = p.value + carry
        carry = value / 10
        ptail.next = SNode(value)
        ptail = ptail.next
        p = p.next
    
    if carry:
        ptail.next = SNode(carry)
    return psum


if __name__ == '__main__':
    phead1 = SNode(0)
    for i in range(6):
        p = SNode(randint(0,9) % 10)
        p.next = phead1.next
        phead1.next = p
    
    phead2 = SNode(0)
    for i in range(9):
        p = SNode(randint(0,9) % 10)
        p.next = phead2.next
        phead2.next = p
    
    print(phead1)
    print(phead2)
    psum = add(phead1, phead2)
    print(psum)
