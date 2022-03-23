import sys
import parse

import fsa

parser = parse.Parser('fsa.txt')

tokens = parser.read_tokens()

if len(tokens) != 5:
    print("error: not proper FSA description in fsa.txt")
    quit()

alphabet = parser.parse_comma(tokens[1])

# # for testing
# print(alphabet)

transitions = parser.parse_transitions(tokens[2])

# # for testing
# print(transitions)

# checks if transitions are defined in alphabet
for transition in transitions:

    # # for testing
    # print(transition[-1])

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

# # for testing
# print(input_string)

file.close()

fsa = fsa.FSA()

states = []

for transition in transitions:
    if transition[0] not in states:
        states.append(transition[0])
    if transition[1] not in states:
        states.append(transition[1])

# # for testing
# print(states)

accept_states = parser.parse_comma(tokens[4])

# # for testing
# print(accept_states)

state_nodes = []

for state in states:
    if state in accept_states:
        state_nodes.append(fsa.create_state(state, True))
    else:
        state_nodes.append(fsa.create_state(state, False))

# # for testing
# for state_node in state_nodes:
#     state_node.print()

transition_nodes = []

for transition in transitions:
    start_state = fsa.search_state(state_nodes, transition[0])
    end_state = fsa.search_state(state_nodes, transition[1])
    transition_nodes.append(fsa.create_transition(start_state, end_state, transition[2]))

# # print transitions for testing
# for transition_node in transition_nodes:
#     transition_node.print()

start_state_number = tokens[3]

start_state = fsa.search_state(state_nodes, start_state_number)
end_state = fsa.traverse_fsa(start_state, transition_nodes, input_string)

end_state.print()

if end_state.is_accept_state():
    print("input string is legal for given FSA")
else:
    print("input string is illegal for given FSA")
