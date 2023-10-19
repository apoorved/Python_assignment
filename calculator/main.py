import sys
import functions

calc_dict = {
    '+': functions.add,
    '-': functions.sub,
    '*': functions.mult,
}

function = sys.argv[1]
first_val = int(sys.argv[2])
second_val = int(sys.argv[3])

output = calc_dict[function](first_val,second_val)
print(output)