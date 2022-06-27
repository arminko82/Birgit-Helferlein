from bottle import route, run, template


@route('/')
def server_static():
    """
    Serves index.
    """
    return static_file("index.html")


run(host='localhost', port=8080)


