import sys
from functions import functions

operation = sys.argv[1]
first_val = int(sys.argv[2])
second_val = int(sys.argv[3])

output = functions[operation](first_val,second_val)
print(output)