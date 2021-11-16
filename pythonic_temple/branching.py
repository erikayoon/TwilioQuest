# Program that accepts 2 command line arguments (integers)
# Should print different things depending on the sum of the two ints

import sys

int1 = int(sys.argv[1])
int2 = int(sys.argv[2])
sum = int1+int2

if sum <= 0:
    print("You have chosen the path of destitution.")
elif sum > 0 and sum < 101:
    print("You have chosen the path of plenty.")
else:
    print("You have chosen the path of excess.")
