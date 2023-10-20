import sys
import argparse
from functions import functions

args_dict = [{'name': 'operand','type': str, 'help':'The operation to be performed *,/,-,+'},
             {'name': 'first_value','type': int, 'help':'The first numerical value'},
             {'name': 'second_value','type': int, 'help':'The second numerical value'}]
try:
    parser = argparse.ArgumentParser()
    for arg in args_dict:
        parser.add_argument(arg['name'], type=arg['type'], help=arg['help'])
    args = parser.parse_args()

except argparse.ArgumentError as e:
    print(e.message)
    sys.exit(1)

operation = args.operand
first_val = args.first_value
second_val = args.second_value

output = functions[operation](first_val,second_val)
print(output)
