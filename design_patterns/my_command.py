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
    def __init__(self):
        self.__order_queue = [] # an empty list which will contain the commands to be executed
    def placeOrder(self, order):
        # we should validate ...
        self.__order_queue.append(order)
        # here we execute the order. We are on a single thread, 
        # but in a multi-threaded or async environment, this might be delayed
        # we might choose to pop the commands as we execute them
        o = self.__order_queue.pop()
        o.execute()

def main():
    '''use the classes to illustrate the command design pattern'''
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke some commands
    agent.placeOrder(buy)
    agent.placeOrder(sell)

if __name__ == '__main__':
    main()