# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python


def pick_peaks(arr):
    #your code here
    i = 1
    pos = []; peaks = []
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            pos.append(i)
            peaks.append(arr[i])
        elif arr[i]>arr[i-1] and arr[i]==arr[i+1]:
            for j in range(i,len(arr)):
                if arr[i]>arr[j]:
                    pos.append(i)
                    peaks.append(arr[i])
                    break
                elif arr[i]<arr[j]:
                    break
    return {'pos':pos, 'peaks':peaks}


# a better solution O(n)
def pick_peaks(arr):
    peaks, pos = [],[]
    ind, val = [],[]
    for i in range(1, len(arr)):
        if arr[i]>arr[i-1]:
            ind, val = [i], [arr[i]]
        elif arr[i]<arr[i-1]:
            pos = pos+ind
            peaks = peaks+val
            ind, val = [],[]
           
    return {'pos':pos, 'peaks':peaks}
