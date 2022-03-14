def colorfulNumber(n):
    digits = [int(d) for d in str(n)]
    prodSet = set()
    for i in range(1,2**len(digits),1):
        subset = bin(i)[2:].zfill(len(digits))
        prod = 1
        for j in range(len(digits)):
            if subset[j] == '1':
                prod *= digits[j]
        if prod in prodSet:
            return False
        else:
            prodSet.add(prod)
    return True

if __name__ == '__main__':
    #n = int(input().strip())
    n = 6
    result = colorfulNumber(6)
    print(result)
    fptr = open('C://Users/iamwl/Documents/projects/colorfulNumberOutput.txt','w')
    fptr.write('{} is {}'.format(6, result))
    fptr.write('\n')
