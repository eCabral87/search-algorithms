# Program: Binary Search
# It needs a sorted array as input
# It runs in O(log2(n))

def binary_search(arr, val_to_find):
# Inputs: arr (1xN)
#      : item (value to find in arr)
# Output: index of item
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high)//2
        if arr[mid] == val_to_find:
            return mid
        elif arr[mid] < val_to_find:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recursive(arr, low, high, val_to_find):
    mid = (low + high) // 2
    if low > high:
        return None
    else:
        if arr[mid] == val_to_find:
            return mid
        elif arr[mid] < val_to_find:
            low = mid + 1
        else:
            high = mid - 1
        return binary_search_recursive(arr, low, high, val_to_find)


if __name__ == "__main__":
    n = 1000000
    item = 566
    array = [i+1 for i in range(n)]
    print(binary_search(array, item))
    print(binary_search_recursive(array, 0, n-1, item))