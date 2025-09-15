# the command design pattern

from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade():
    '''low-level buy and sell operations'''
    def buy(self):
        print('Buy stocks')
    def sell(self):
        print('Sell stock')

class BuyStock(Order):
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock)== StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.buy()

class SellStock(Order):
    def __init__(self, stock):
        self.stock = stock
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, new_stock):
        if type(new_stock)== StockTrade:
            self.__stock = new_stock
        else:
            raise TypeError('Missing required stock trade instance')
    def execute(self):
        return self.stock.sell()

class Agent:
    '''The agent will issue commands'''


def main():
    '''use the classes to illustrate the command design pattern'''

if __name__ == '__main__':
    main()