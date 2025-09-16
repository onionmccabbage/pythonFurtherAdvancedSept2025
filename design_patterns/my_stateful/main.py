from _on import On
from _off import Off
from _sleep import Sleep
from _hybernate import Hybernate
from _device import Laptop

def main():
    '''exercise the code'''
    c = Laptop()
    c.change(On)
    c.change(Off)
    c.change(Sleep) # fail
    c.change(On)
    c.change(Sleep)
    c.change(Hybernate)
    c.change(On)

if __name__ == '__main__':
    main()