
# A very simple Bottle Hello World app for you to get started with...
import datetime
import time
import os
import pymongo
from bson.objectid import ObjectId

# are we executing at PythonAnywhere?
ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ

# assert ON_PYTHONANYWHERE == False

if ON_PYTHONANYWHERE:
    # from bottle import default_app
    from bottle import default_app
else:
    from bottle import run, debug

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.yg7xt.mongodb.net/todo?retryWrites=true&w=majority",
                            connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             # socketKeepAlive=True,
                             connect=False, maxPoolsize=1)


db = client.todo

from bottle import get, post, request, response, template, redirect, default_app

# APPLICATION PAGES AND ROUTES

# assume collection contains fields "id", "task", "status"

@get('/')
def get_show_list():
    result = db.task.find()
    # return list(result)
    # get all the items in the collection as a list of dictionaries
    return template("mongodb/show_list", rows=result, session={})


@get('/update_status/<_id>/<value:int>')
def get_update_status(_id, value):
    result = db.task.update_one( {"_id" : ObjectId(_id)}, {'$set': {'status': (value!=0)}} )
    redirect('/')


@get('/delete_item/<_id>')
def get_delete_item(_id):
    # given an id, delete the relevant document
    result = db.task.delete_one( {"_id": ObjectId(_id)} )
    redirect('/')


@get('/update_task/<_id>')
def get_update_task(_id):
    # given an id, get the document and populate a form
    result = db.task.find_one( {"_id": ObjectId(_id)} )
    return template("mongodb/update_task", row=dict(result))

@post('/update_task')
def post_update_task():
    # given an id and an updated task in a form, find the document and modify the task value
    _id = request.forms.get("_id").strip()
    updated_task = request.forms.get("updated_task").strip()
    result = db.task.update_one( {"_id" : ObjectId(_id)}, {'$set': {'task': updated_task}} )
    redirect('/')

@get('/new_item')
def get_new_item():
    return template("new_item")


@post('/new_item')
def post_new_item():
    # given a new task in a form, create and insert a document and with that task value
    new_task = request.forms.get("new_task").strip()
    result = db.task.insert_one( {'task': new_task, 'status':False} )
    redirect('/')

application = default_app()


if ON_PYTHONANYWHERE:
    # on Pa, connect to the WSGI Server
    application = default_app()
    pass
else:
    # on the dev env
    debug(True)  # comment out
    run(host='localhost', port=8080)  # comment out
# if __name__ == "__main__":
#     #db.tasks.insert_one({'id':1, 'task':"read a book on Mongo", "status":False})
#     #db.tasks.insert_one({'id':2, 'task':"read a another book on PyMongo", "status":False})
#     print(get_show_list())