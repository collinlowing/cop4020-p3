class Transition:
    __start_state = None
    __end_state = None
    __alpha = None

    def __init__(self, start_state, end_state, alpha):
        Transition.__start_state = start_state
        Transition.__end_state = end_state
        Transition.__alpha = alpha

    def get_start_state(self):
        return Transition.__start_state

    def get_end_state(self):
        return Transition.__end_state

    def get_alpha(self):
        return Transition.__alpha