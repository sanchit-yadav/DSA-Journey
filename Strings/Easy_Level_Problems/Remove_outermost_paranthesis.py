# Remove outer most paranthesis from a valid string of paranthesis

def remove_outermost_parentheses(s):
    result = []
    open_count = 0

    for char in s:
        if char == '(':
            if open_count > 0:
                result.append(char)
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count > 0:
                result.append(char)

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    input_string = "(()())(())"
    output_string = remove_outermost_parentheses(input_string)
    print(output_string)