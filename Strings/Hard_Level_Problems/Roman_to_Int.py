# Problem : Given a roman numeral, convert it to an integer.

def roman_to_int(s:str):
    values = {'I':1, 'V':5, 'X':10, 'L':50,
              'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        val = values[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

#Example Usage
if __name__ == "__main__":
    print(roman_to_int("MCMXCIV")) 
    print(roman_to_int("LVIII"))
    print(roman_to_int("IX"))    
    print(roman_to_int("IV"))  