# Problem : Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

def MaxDepth(s:str):
    result = 0
    count = 0
    for ch in s:
        if ch=="(":
            count+=1
            result = max(count, result)
        elif ch==")":
            count-=1
    return result

#Example Usage
if __name__ == "__main__":
    string = "()(())((()()))"
    print(MaxDepth(string))
    string = "(1+(2*3)+((8)/4))+1"
    print(MaxDepth(string))
    string = "(1)+((2))+(((3)))"
    print(MaxDepth(string))