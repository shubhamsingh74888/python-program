def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index of the target
    return -1  # Not found

# Input: Array and target element
user_input = input("Enter the elements of the array (space-separated): ")
arr = list(map(int, user_input.split()))
target = int(input("Enter the number to search for: "))

# Perform search
index = linear_search(arr, target)

# Output result
if index != -1:
    print(f"{target} found at index {index}.")
else:
    print(f"{target} not found in the array.")
