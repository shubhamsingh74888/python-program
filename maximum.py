# Function to find the greatest number
def find_greatest(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Input: list of numbers from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Find and display the greatest number
greatest = find_greatest(numbers)
print(f"The greatest number is: {greatest}")
