import sys

str1 = sys.argv[1] if len(sys.argv) > 1 else input("Enter a string: ")

rev = str1[::-1]

if str1 == rev:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")