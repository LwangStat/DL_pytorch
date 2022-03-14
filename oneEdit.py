def oneEditApart(str1, str2):
    if len(str1) == len(str2):
        d = 0
        for i in range(len(str1)):
            if not str1[i] == str2[i]:
                d += 1
        if d ==1:
            return True
        else:
            return False  
    elif len(str1) == len(str2) - 1:
        skip = 0
        i = 0
        while skip < 2 and i < len(str1):
            if str1[i] == str2[i+skip]:
                i +=1
            else:
                skip +=1
        if skip > 1:
            return False
        else:
            return True
    elif len(str1) == len(str2) + 1:
        skip = 0
        i = 0
        while skip < 2 and i < len(str2):
            if str2[i] == str1[i+skip]:
                i +=1
            else:
                skip +=1
        if skip > 1:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    print(oneEditApart("cats", 'cats'))