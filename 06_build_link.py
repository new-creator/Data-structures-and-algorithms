class Listnode():
    def __init__(self, val):
        self.val = val
        self.next = None


def build_link(arr):
    new = cur = Listnode(0)
    for i in arr:
        cur.next = Listnode(i)
        cur = cur.next
    return new.next

new = [1,2,3,2,1]
new = build_link(new)