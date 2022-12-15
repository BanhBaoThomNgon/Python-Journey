"""Calculate Gregorian Easter using Gauss's algorithm."""

import sys


def easter_date(y):
    a = y % 19
    b = y % 4
    c = y % 7
    k = (y/100)
    p = (13 + 8 * k) / 25
    q = k / 4
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    r = 22 + d + e
    s = d + e - 9

if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    print(easter_date(year))