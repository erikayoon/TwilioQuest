# Code must declare 4 variables which are the result of math operations performed
# on the two numbers passed in to the script as command line arguments

import sys

# This code reads in arguments and converts those inputs into decimal numbers
first_number = float(sys.argv[1])
second_number = float(sys.argv[2])

# My code starts here:
result_sum = first_number + second_number
result_difference = first_number - second_number
result_product = first_number * second_number
result_quotient = first_number / second_number