# Manipulate a string of text to take the first argument and transform it 
# 1) All Uppercase Letters
# 2) Append 3 exclamation points

import sys

print(f"{sys.argv[1].upper()}!!!")

"""
This also works:
print(sys.argv[1].upper() + "!!!")
""" 
