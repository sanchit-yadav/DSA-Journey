# Problem: Find second largest element in an array without sorting the array.
def second_Largest(arr):
    if len(arr) < 2:
        return None  # Return None if there are less than 2 elements
    first = second = float('-inf')  # Initialize first and second largest to negative infinity
    for num in arr:
        if num > first:
            second = first  # Update second largest
            first = num  # Update largest
        elif first > num > second:
            second = num  # Update second largest if num is between first and second
    return second if second != float('-inf') else None  # Return None if no second largest found

# Example usage:
if __name__ == "__main__":
    array = [1, 8, 7, 56, 90]
    result = second_Largest(array)
    if result is not None:
        print("The second largest element in the array is:", result)
    else:
        print("There is no second largest element in the array.")