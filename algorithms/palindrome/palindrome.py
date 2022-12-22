def isPalindrome(x) -> bool:
    reverse = x[::-1]
    if (x == reverse):
        print("True")
    else:
        print("False")

isPalindrome()