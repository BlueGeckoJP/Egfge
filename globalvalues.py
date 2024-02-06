import os


class GlobalValues:
    current_path = ""
    current_moving_index = 0
    moving_history: list[str] = []

    def init(self):
        gv = type(self)
        gv.current_path = os.path.expanduser("~")
        gv.current_moving_index = 0
        gv.moving_history = [os.path.expanduser("~")]
