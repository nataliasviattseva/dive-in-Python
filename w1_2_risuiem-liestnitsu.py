import sys

digit_string = int(sys.argv[1])

for i in range(digit_string):
    print(" " * (digit_string - i) + "#" * (i + 1))
