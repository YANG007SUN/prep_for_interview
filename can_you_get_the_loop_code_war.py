
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    c = 0
    d = {}
    nxt = node.next
    d[nxt] = 0
    while 1:
        nxt = nxt.next
        if nxt in d:
            return c- d[nxt]+1
        c+=1
        d[nxt] = c