from math import isqrt


def get_divisors(number: int) -> list[int]:
    """Return the positive divisors of a positive integer in ascending order."""
    if number <= 0:
        raise ValueError("number must be positive")

    divisors = []
    for candidate in range(1, isqrt(number) + 1):
        if number % candidate == 0:
            # Divisors occur in pairs: candidate and number // candidate.
            divisors.append(candidate)
            paired_divisor = number // candidate
            if paired_divisor != candidate:
                divisors.append(paired_divisor)

    return sorted(divisors)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(get_divisors(number))
