# Function to implement linear search
def linear_search(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index  # Return the index if the element is found
    return "Not found"  # Return "Not found" if the element is not found

# Input: Array of integers
arr = list(map(int, input().split()))

# Input: Key element to search for
key = int(input())

# Call the linear_search function and print the result
result = linear_search(arr, key)
print(result)
