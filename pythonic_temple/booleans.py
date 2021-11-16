# Create a program that declares several boolean variables
# If the first argument to the script is exactly "For the glory of Python!"
# then the third variable should be set to True
import sys

python_is_glorious = True
failure_is_option = False
proper_greeting = False

if sys.argv[1] == "For the glory of Python!":
    proper_greeting = True