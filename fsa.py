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

    def search_state(self, states: list[state.State], number):
        for s in states:
            if s.get_number() == number:
                return s

    # def traverse_fsa(self, starting_state, transitions, string):
    #     current_state = starting_state
    #     for char in string:
    #         for t in transitions:
    #             if t.get_alpha() == char and starting_state == t.get_start_state:
    #                 current_state = t.get_end_state
    #
    #     return current_state
