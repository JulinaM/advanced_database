import os
from bottle import get, post, template, request, redirect

import sqlite3

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

# assert ON_PYTHONANYWHERE == False

if ON_PYTHONANYWHERE:
    # from bottle import default_app
    from bottle import default_app
else:
    from bottle import run, debug


@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)

@get('/set_status/<id:int>/<value:int>')
def get_set_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id))
    connection.commit()
    cursor.close()
    redirect("/")

@get('/environ')
def get_environ():
    return str(os.environ)


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

@get("/update_item/<id:int>")
def get_update_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id, ))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result[0])

@post("/update_item")
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_item, id))
    connection.commit()
    cursor.close()
    redirect("/")

@get('/delete_item/<id:int>')
def delete_item(id):
    print('We  want to delete item ', id)
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todo WHERE id=?", (id,))
    connection.commit()
    cursor.close()
    # return "The new item is [" + str(new_item) + "]..."
    redirect("/")

    pass


if ON_PYTHONANYWHERE:
    # on Pa, connect to the WSGI Server
    application = default_app()
    pass
else:
    # on the dev env
    debug(True)  # comment out
    run(host='localhost', port=8080)  # comment out
