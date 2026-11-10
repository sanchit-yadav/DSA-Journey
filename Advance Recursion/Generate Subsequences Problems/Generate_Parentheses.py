# Problem : Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

# Example usage:
if __name__ == "__main__":
    n = 3
    print(generate_parentheses(n))