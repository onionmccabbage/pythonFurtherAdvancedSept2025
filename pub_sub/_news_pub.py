class newsPublisher():
    def __init__(self):
        '''publis a stream of events, e.g. news stories'''
        self.__subscribers = [] # an empty list
        self.latest_news = None
    # Observables expose methods for 'attach' and 'detach' events
    def attach(self, new_sub):
        self.__subscribers.append(new_sub) # probably worth validating here
    def detach(self):
        self.__subscribers.pop() # pop will remove the top-most member of the list
    def iter_subscribers(self):
        '''use a list comprehension to iterate the subscribers'''
        return [type(x).__name__ for x in self.__subscribers]
    def notify_sub(self):
        for sub in self.__subscribers:
            sub.update()
    def add_news(self, news):
        self.latest_news = news
    def get_news(self):
        return f'News just in: {self.latest_news}'