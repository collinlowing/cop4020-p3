import re
import state
import transition

class FSA:
    def get_pattern(self, transitions):
        pass

    def check_string(self, pattern, string):
        match = re.search(pattern, string)

        if match:
            print("string is legal")
        else:
            print("string is illegal")

        return match

    def create_state(self, number, accept):
        new_state = state.State(number, accept)
        return new_state

    def create_transition(self, start_state, end_state, alpha):
        new_transition = transition.Transition(start_state, end_state, alpha)
        return new_transition
