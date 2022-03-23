class State:
    __number = None
    __accept = False

    def __init__(self, number, accept):
        State.__number = number
        State.__accept = accept

    def get_number(self):
        return State.__number

    def is_accept_state(self):
        return State.__accept
