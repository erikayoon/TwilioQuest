# Write a script that can accept any number of command line arguments
# For all arguments that are passed to the script, print out the list item
# prepended with their order

"""
Example Execution: 
python3 list_iteration.py Deak Windy Luke Biggs

Output:
1. Deak
2. Windy
3. Luke
4. Biggs
"""

import sys

index = 1
for name in sys.argv[1:]:
    print(str(index) + ". " + name)
    index += 1
