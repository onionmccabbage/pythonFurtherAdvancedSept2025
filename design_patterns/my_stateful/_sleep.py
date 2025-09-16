from _device_state import ComputerState

class Sleep(ComputerState):
    name='Sleep'
    allowed = ['On', 'Hybernate']