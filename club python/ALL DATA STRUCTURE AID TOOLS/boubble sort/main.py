x= [23,41,33,81,7,19,11,45]

def boubbleSort():
    n = len(x)
    swap = True
    while(swap):
        swap = False
        for j in range(0, n-1):
            if (x[j] > x[j+1]):
                swaper(j, j+1)
                swap = True

def swaper(a, b):
    first = x[a]
    second = x[b]
    x[a] = second
    x[b] = first

boubbleSort()
print(x)

