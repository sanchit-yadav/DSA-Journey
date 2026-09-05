def is_palindrome(number: int) -> bool:
    """Return whether number reads the same forwards and backwards."""
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        # Extract the last digit and append it to the reversed number.
        last_digit = number % 10
        reversed_number = (reversed_number * 10) + last_digit
        number //= 10

    return original == reversed_number


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(is_palindrome(number))
