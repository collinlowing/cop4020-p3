class State:
    __number = None
    __accept = False

    def __init__(self, number, accept):
        self.__number = number
        self.__accept = accept

    def get_number(self):
        return self.__number

    def is_accept_state(self):
        return self.__accept

    def print(self):
        if self.__accept:
            print("State " + self.__number + " is accept state")
        else:
            print("State " + self.__number + " is not accept state")
