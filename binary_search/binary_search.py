
def binary_search(arr, item):
# Inputs: arr (1xN)
#      : item (value to find in arr)
# Output: index of item
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low =  mid + 1
        else:
            high = mid - 1
    return None


# TODO
#def binary_search_recursive(arr, item):
         

if __name__ == "__main__":
    n = 1000
    item = 566
    print(binary_search([i+1 for i in range(n)], item))