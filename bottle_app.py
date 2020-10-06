import os
from bottle import get, post, template, request, redirect

from storage import get_items, get_item, update_status, create_item, update_item, delete_item


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
    result = get_items()
    return template("show_list", rows=result)

@get('/set_status/<id:int>/<value:int>')
def get_set_status(id, value):
    update_status(id, value)
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
    create_item(new_item,1)
    # return "The new item is [" + str(new_item) + "]..."
    redirect("/")

@get("/update_item/<id:int>")
def get_update_item(id):
    result = get_item(id)
    return template("update_item", row=result)

@post("/update_item")
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    update_item(id, updated_item)
    redirect("/")

@get('/delete_item/<id:int>')
def delete_item(id):
    print('We  want to delete item ', id)
    delete_item(id)
    redirect("/")


if ON_PYTHONANYWHERE:
    # on Pa, connect to the WSGI Server
    application = default_app()
    pass
else:
    # on the dev env
    debug(True)  # comment out
    run(host='localhost', port=8080)  # comment out
