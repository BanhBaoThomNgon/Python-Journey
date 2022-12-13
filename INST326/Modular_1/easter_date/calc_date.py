"""Calculate Gregorian Easter using Gauss's algorithm."""

import sys
import math


# replace this comment with your implementation of the easter_date() function
def easter_date(year):
    y = year
    a = y % 19
    b = y % 4
    c = y % 7
    k = math.floor(y / 100)
    p = math.floor(13 + 8 * k) / 25
    q = math.floor(k / 4)
    m = math.floor(15 - p + k - q) % 30
    n = math.floor(4 + k - q) % 7
    d = math.floor(19 * a + m) % 30
    e = math.floor(2*b + 4*c + 6*d + n) % 7
    r = 22 + d + e
    s = d + e - 9

    if (d == 29 and e == 6 and s == 26):
        return("April 19")
    elif (d == 28 and e == 6 and (11*m + 11) % 30 < 19 and s == 25):
         return("April 18")
    elif (s > 0):
        return("April " + str(s))
    else:
        return("March " + str(r))




if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    print(easter_date(year))