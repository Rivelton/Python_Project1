import copy

n = 10 #int(input())
arr = [6,6,6,6,6,6,6,6,6,5] #list(map(int, input().split()))
q = copy.deepcopy(arr)

arr.sort(reverse=True)

while n:
    if arr[0] == arr[1]:
        arr.pop(0)
    else:
        break
if arr[0] > arr[1]:
    arr.pop(0)
resp = arr[0]

print(resp)





