# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python

# ========================================================================
# recur method - return the last survisor
# Function takes three parameters
# t = list, k = # to skip to kill, st = starting index in the list
def w(t, k, st):
    if len(t) == 1:
        return t[o]
    st = (st+k-1)%len(t)
    t.remove(t[st])
    return w(t, k, st)

# return the the list of killed people in order
# Function takes two parameter, 
# return to list of killed people in order
def josephus(t, k):
    st, output = 0, []
    while len(t)>0:
        st = (st+k-1)%len(t)
        output.append(t.pop(st))
    return output



