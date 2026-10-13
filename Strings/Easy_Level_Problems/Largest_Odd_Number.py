# Problem : Find the lartest odd number from a string containing numbers.

def Largest_Odd(s):
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 1:
            return s[0:i+1]
    return ""

#Example Usage
if __name__ == "__main__":
    str1 = "125782"
    str2 = "246846"
    str3 = "8974586237"
    str4 = "00000"
    print(Largest_Odd(str1))
    print(Largest_Odd(str2))
    print(Largest_Odd(str3))
    print(Largest_Odd(str4))