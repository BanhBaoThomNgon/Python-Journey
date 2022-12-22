roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}

test1 = 'IV'
test2 = 'LVIII'
test3 = 'MCMXCIV'

def romanToInt(romanNumeral):
    output = 0
    length = len(romanNumeral)
    for i in reversed(range(length)):
        if i == length - 1:
            output += roman[romanNumeral[i]]
        elif roman[romanNumeral[i]] < roman[romanNumeral[i + 1]]:
            output -= roman[romanNumeral[i]]
        else:
            output += roman[romanNumeral[i]]
    return output

print(romanToInt(test1))
print(romanToInt(test2))
print(romanToInt(test3))