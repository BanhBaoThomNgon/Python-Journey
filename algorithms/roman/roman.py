roman_dictionary = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
# only I X and C can be subtractive


numeral = "IIIL"

numeral_arr = []

for i in range(len(numeral)):
    key = numeral[i]
    if key in roman_dictionary:
        numeral_arr.append(roman_dictionary[key])
    else:
        print("There was an error, " + key + "is not a roman numeral")
        break

for i in range(len(numeral_arr)):
    limit = len(numeral_arr)
    if (i == limit):
        # do the last addition/subtraction
        break
    if (numeral_arr[i] > numeral_arr[i+1]):
        # print(numeral_arr[i] + numeral_arr[i+1])
        print(numeral_arr[i] + numeral_arr[i+1])
    else:
        print("there was an error")
        break