# ============================================
# counting number of negative values in lists
# ============================================


# ---------------------------------------------------------
# fist input takes a integer of number of rows in the array
# rest of inputs are the numbers separated by space
# ---------------------------------------------------------


# -------------------------------------------------------------
# This is the optimal solution to count negatives in the array
# Time complexity it takes is O(m+n)
# Sorting the list first, then count from the end of the list
# -------------------------------------------------------------


def count_negative(l:list)->int:
    """counting number of negative values in 2D list
    """
    res = []
    m = len(l) # number of rows
    n = len(l[0]) # number of columns
    
    #sort the list from lowest to highest
    for i in range(m):
        l[i] = sorted(l[i])
    
    for i in range(m):
        for j in range(n-1, -1, -1):
            if l[i][j]<0:
                res.append(j+1)
                break
            
    print(sum(res))

# number of rows
m = int(input())
l = []
for _ in range(m):
    l.append(list(map(int, input().split())))

count_negative(l)






