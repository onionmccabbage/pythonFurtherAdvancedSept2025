class Sub():
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)
    # NB make sure this is indented correctly
    def update(self):
        print(type(self).__name__, self.publisher.get_news())