def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1
def Rotate(a, d):
    if d == 0:
        return
    n = len(a)
    d = d % n
    reverseArray(a, 0, d - 1)
    reverseArray(a, d, n - 1)
    reverseArray(a, 0, n - 1)
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
a= [10, 20, 13, 24, 53, 6, 17]
n = len(a)
d = 2
printArray(a)
Rotate(a, d)
print("\nreversel array: ")
printArray(a)