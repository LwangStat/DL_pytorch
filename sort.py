def mergeSort(l):
    if len(l) == 1:
        return l
    else:
        left = mergeSort(l[:int(len(l)/2)])
        right = mergeSort(l[int(len(l)/2):])
        result = []
        lp = 0
        rp = 0
        while lp < len(left) and rp < len(right):
            if left[lp] <= right[rp]:
                result.append(left[lp])
                lp += 1
            else:
                result.append(right[rp])
                rp += 1
        if lp == len(left):
            result.extend(right[rp:])
        else:
            result.extend(left[lp:])
        return result

def quickSort(l,start,end):
    if start >= end:
        return
    else:   
        lp = start
        rp = end
        pivot = l[int((lp+rp)/2)]
        while lp < rp:
            while l[lp] < pivot:
                lp += 1
            while l[rp] > pivot:
                rp -= 1
            if lp <= rp:
                l[lp], l[rp] = l[rp], l[lp]
                lp +=1
                rp -=1
        quickSort(l,start,rp)
        quickSort(l,lp,end)


if __name__ == '__main__':
    a = [3,6,2,7,7]
    #print(mergeSort(a))
    quickSort(a,0,4)
    print(a)


     