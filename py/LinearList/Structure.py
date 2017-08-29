class Node(object):
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