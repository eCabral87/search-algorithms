
def simple_search(arr, item):
# Inputs: arr (1xN)
#      : item (value to find in arr)
# Output: index of item
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None


if __name__ == "__main__":
    n = 1000
    item = 566
    print(simple_search([i+1 for i in range(n)], item))