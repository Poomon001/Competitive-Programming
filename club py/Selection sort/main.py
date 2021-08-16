x = [5, 1,2, 4,6,3,66,101,44,23,33,44]

def selectionSort():
    for i in range(0, len(x)-1):
        min = i # i = 0, x[i] = 5
        for j in range(i + 1, len(x)):
            print(i)
            ''' find min and keep its index'''
            if x[j] < x[min]: #x[j] = 1, x[min] = 5
                min = j # min = 1 + 1 = 2
        swap(i, min) # swap x[i], with x[min] ===> 1, 5, 2, 3, 4, 1, 2, 52, 10, 39, 42, 42

def swap(i, min):
    first = x[i]
    second = x[min]
    x[min] = first
    x[i] = second

selectionSort()
print(x)



