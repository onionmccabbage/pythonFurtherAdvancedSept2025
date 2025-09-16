from _device_state import ComputerState

class Off(ComputerState):
    name='Off'
    allowed = ['On']