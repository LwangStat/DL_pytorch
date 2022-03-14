def moveRight(arr, i, j, value):
    while j < len(arr) and arr[i][j] == 0:
        arr[i][j] = value
        j += 1
        value +=1
    return i+1, j-1, value

def moveDown(arr, i, j, value):
    while i < len(arr) and arr[i][j] == 0:
        arr[i][j] = value
        i += 1
        value +=1
    return i-1, j-1, value

def moveLeft(arr, i, j, value):
    while j >= 0 and arr[i][j] == 0:
        arr[i][j] = value
        j -= 1
        value +=1
    return i-1, j+1, value

def moveUp(arr, i, j, value):
    while i >= 0 and arr[i][j] == 0:
        arr[i][j] = value
        i -= 1
        value +=1
    return i+1, j+1, value 

def spiral(n):
    arr = [[0]*n for i in range(n)]
    value = 0
    i, j, value = 0, 0, 1
    while value <= n**2:
        i, j, value = moveRight(arr, i, j, value)    
        i, j, value = moveDown(arr, i, j, value)
        i, j, value = moveLeft(arr, i, j, value)
        i, j, value = moveUp(arr, i, j, value)
    print(arr)

if __name__ == '__main__':
    spiral(6)