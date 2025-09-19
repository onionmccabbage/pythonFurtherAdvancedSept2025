from flask import Flask # we may need to pip install Flask
from flask import render_template, request
# Flask is a full-featured BASIC web server. It efficiently handles web request and serves responses
# flask contains a micro-syntax for configuring response objects

# Caution: flask is a development server with NO seciruty features
# to deploy flask you would add it to a secure server
def main():
    '''here is a simple Flask web server'''
    app = Flask(__name__)
    # we declare routes for the web server
    @app.route('/') # the entry point of the server
    def root():
        return 'Hello'
    @app.route('/greet')
    def greet():
        return '<h3>Greetings from Flask</h3>'
    @app.route('/info')
    @app.route('/about')   # common mis-spellings, or different brand names for a feature, or changes...
    @app.route('/details') # any of those routes will end up on this page
    def generic():
        return '<p>Information about stuff</p>'
    # a truly RESTful URL allowes parameters in the URL
    @app.route('/category')
    @app.route('/category/<cat>') # these values in <> are injected as REST values
    @app.route('/category/<cat>/<id>')
    def category(cat='people', id=1): # we provide sensible default values
        return f'Category is {cat} id is {id}'
    # here is a route which will invoke an HTML template
    @app.route('/menu')
    @app.route('/menu/<specials>')
    def menu(specials=None):
        # NB we need to pass any REST arguments to the template
        return render_template('menu.html', specials=specials)
    # see https://www.browserstack.com/guide/flask-get-query-parameters
    @app.route('/user')
    def user():
        # NB remember to import request from Flask
        name = request.args.get('name')  # /user?name=John
        return f"Hello, {name}"
    # we start the Flask server like this
    # debug=True will make a watching-server: any changes will cycle the server
    app.run(debug=True) # a run-loop is started and the server is invoked

if __name__ == '__main__':
    main()