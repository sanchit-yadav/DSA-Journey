def is_armstrong(number: int) -> bool:
    """Return whether number is an Armstrong number."""
    if number < 0:
        return False

    digits = len(str(number))
    remaining = number
    total = 0

    while remaining > 0:
        # Add each digit raised to the total number of digits.
        last_digit = remaining % 10
        total += last_digit**digits
        remaining //= 10

    return total == number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(is_armstrong(number))
