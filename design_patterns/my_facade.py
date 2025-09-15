# a facade is also a single-point-of-access to several disparate entities

class Coder: # NB usually aim to write classes in separate modules
    'write some code'
    def __init__(self):
        print('coder writes some code')
    def __is_available(self):
        return True # we may have some logic to determine availability
    def book_time(self):
        if self.__is_available():
            print('coder is available and has been booked')

class Tester:
    '''configure tests'''
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place for due diligence')

class Technician:
    '''do technical stuff'''
    def __init__(self):
        print('preparing equipment for the team')
    def doTechyStuff(self):
        print('equipment is is in place and configured')

class Artisan:
    '''design capabilities'''
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')

class Manager:
    'the manager is the facade to these different classes. They are sufficiently different to use a facade'
    def __init__(self):
        print('The manager says I can arrange the team')
    def arrange(self):
        '''The facade provides isntances of all the other subsystems/microservices'''
        self.coder      = Coder()
        self.technician = Technician()
        self.tester     = Tester()
        self.artisan    = Artisan()
        # .. plus any additional assets we may need....
        self.coder.book_time()
        self.tester.testing()
        self.technician.doTechyStuff()
        self.artisan.make_prototype()

if __name__ == '__main__':
    manager = Manager() # this is our facade
    manager.arrange() # get things going