def is_palindrome(str, left, right):
    if left >= right:    # crossed over → all pairs matched
        return True
    if str[left] != str[right]:   # mismatch
        return False
    # move both pointers inward
    return is_palindrome(str, left + 1, right - 1)

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    # check the whole string
    result = is_palindrome(input_str, 0, len(input_str) - 1)
    print(f"Is the string '{input_str}' a palindrome? {result}")