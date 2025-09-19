from flask import Flask # we may need to pip install Flask

# Flask is a full-featured BASIC web server. It efficiently handles web request and serves responses
# flask contains a micro-syntax for configuring response objects

# Caution: flask is a development server with NO seciruty features
# to deploy flask you would add it to a secure server
def main():
    '''here is a simple Flask web server'''
    app = Flask(__name__)

    # we start teh Flask server like this
    app.run() # a run-loop is started and the server is invoked

if __name__ == '__main__':
    main()