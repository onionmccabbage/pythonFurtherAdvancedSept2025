from _news_pub import newsPublisher
from _email_sub import EmailSub
from _print_sub import PrintSub
from _media_sub import MediaSub
from _qos_sub import QoS

# here we have a global tuple
subs_t = (EmailSub, PrintSub, MediaSub, QoS)

def main():
    '''invoke the parts of our project'''
    news_pub = newsPublisher()
    for subscriber in subs_t:
        subscriber(news_pub)
        # we could usse a separate loop to add news
        news_pub.add_news('News flash - its nearly time to do something exciting!!')
    # we can notify all the subscribers
    news_pub.notify_sub() # they all get notified

if __name__ == '__main__':
    main()