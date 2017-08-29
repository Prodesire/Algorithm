from random import randint


class Node(object):
    def __init__(self, value):
        self.value = int(value)
        self.next = None

    def __len__(self):
        length = 1
        p = self
        while p.next:
            length += 1
            p = p.next
        return length

    def __bool__(self):
        return self is not None

    def __str__(self):
        p = self
        if not p:
            return ''

        output = str(p.value)
        while p.next:
            output += '->{}'.format(p.next.value)
            p = p.next
        return output


def gen_linkedlist(length, maxint=9, with_tail=False):
    pcur = phead = Node(0)
    for i in range(length):
        pcur.next = Node(randint(0, maxint))
        pcur = pcur.next

    if with_tail:
        return phead, pcur
    return phead
