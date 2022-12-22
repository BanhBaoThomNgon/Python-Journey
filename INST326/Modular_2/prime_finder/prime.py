import math
import sys
prime_dict = [2, 3, 5, 7, 11]

for i in range(95):
    prime_dict.append((6 * i + 1))

def is_prime(number):
    if number in prime_dict:
        print("It's a prime number.")
    else:
        print("Sorry, try a different number.")

def main(number):
    is_prime(number)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])