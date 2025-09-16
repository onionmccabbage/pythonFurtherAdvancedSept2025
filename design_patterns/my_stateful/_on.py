from _device_state import ComputerState

class On(ComputerState):
    name='On'
    allowed = ['Off', 'Sleep' 'Hybernate']