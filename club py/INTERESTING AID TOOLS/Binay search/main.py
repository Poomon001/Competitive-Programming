li = [-5,-1, 0, 1, 4, 7, 11, 9, 8, 10, 50, 100, 101, 102]

def binarySearch(li, key):
    newLi = li[:]
    newLi.sort()

    max = len(newLi) - 1
    min = 0
    found = False

    while(not found and max>=min):
        half = (max + min) // 2

        if (key == newLi[half]):
            found = True
            break;

        elif(key < newLi[half]):
            max = half-1
            continue

        elif(key > newLi[half]):
            min = half+1
            continue

    return found

print(binarySearch(li, -5))