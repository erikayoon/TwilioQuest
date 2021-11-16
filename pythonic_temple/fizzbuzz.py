"""
Create a program that accepts any number of command line arguments.
The arguments will be whole/integer numbers. Your script will need to 
examine all these numbers and execute the following conditional logic:
 If the number is divisible by 3, print the text: fizz
 If the number is divisible by 5, print the text: buzz
 If the number is divisible by both 3 and 5, print the text: fizzbuzz
 If none of the above are true, print the number
"""

import sys

for input in sys.argv[1:]:
    input = int(input)
    if input%3==0 and input%5==0:
        print("fizzbuzz")
    elif input%3==0:
        print("fizz")
    elif input%5==0:
        print("buzz")
    else:
        print(input)