from bottle import route, run, template


@route('/<name>')
def index(name):
    return template('<b>Hello {{name}} from index page!!! </b>!', name=name)


@route('/hello')
@route('/hello/<my_name>')
def get_hello(my_name="unknown person"):
    return template('<b>Hello {{name}}</b>!', name=my_name)


@route('/goodbye')
def get_goodbye():
    return "<html>Goodbye there!!</html>"


run(host='localhost', port=8080)
