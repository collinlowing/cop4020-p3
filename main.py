import sys
import parse

import fsa

parser = parse.Parser('fsa.txt')

tokens = parser.read_tokens()

if len(tokens) != 5:
    print("error: not proper FSA description in fsa.txt")
    quit()

alphabet = parser.parse_comma(tokens[1])

print(alphabet)

transitions = parser.parse_transitions(tokens[2])

print(transitions)

# checks if transitions are defined in alphabet
for transition in transitions:
    print(transition[-1])
    if transition[-1] not in alphabet:
        print("alpha" + transition[-1] + "is not defined")
    # else:
    #     print("matched alphabet with state")

argc = len(sys.argv)

if argc < 2:
    print("error: no commandline arguments")
    quit()

input_filename = sys.argv[1]
file = open(input_filename, "r")
input_string = file.readline()
print(input_string)
file.close()

fsa = fsa.FSA()

print(fsa.create_state(0, False))
print(fsa.create_state(0, False))
