# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. 
# For example, given [10, 7, 76, 415], you should return 77641510.

arr = [10, 7, 76, 415]
# rearrange items to make the biggest number
# look at the first integer of each
# if larger, insert and compare next
# if same, compare next two items in each integer
# if ints aren't the same size, compare the string? This needs more thinking

def order(arr):
    if arr[0] >= arr[1]:
        arr.append(arr.pop(0))

# base case
if len(arr) <= 1:
    print(arr)

order(arr)

# print solution
for i in arr:
    print(i, end="", flush=True)



