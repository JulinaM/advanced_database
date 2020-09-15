from bottle import get, post, run, template, request, debug,redirect
import sqlite3


@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)


@get("/new_item")
def get_new_item():
    return template("new_item")


@post("/new_item")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    connection.execute("INSERT INTO todo(task, status) VALUES (?, ?)", (new_item, 1))
    connection.commit()
    connection.close()
    # return "The new item is [" + str(new_item) + "]..."
    redirect("/")

debug(True) #comment out
run(host='localhost', port=8080) #comment out

# application = default_app() # to host
