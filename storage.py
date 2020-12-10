import sqlite3

def get_items():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return result

def get_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id, ))
    result = cursor.fetchall()
    cursor.close()
    return result[0]

def update_status(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?", (value, id))
    connection.commit()
    cursor.close()

def create_item(task, status ):
    connection = sqlite3.connect("todo.db")
    connection.execute("INSERT INTO todo(task, status) VALUES (?, ?)", (task, status))
    id = cursor.lastrowid
    connection.commit()
    connection.close()
    # return "The new item is [" + str(new_item) + "]..."
    return id

def update_item(id, updated_item):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_item, id))
    connection.commit()
    cursor.close()

def delete_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todo WHERE id=?", (id,))
    connection.commit()
    cursor.close()

def test_get_items():
    print("Testing get_items")
    results = get_items()
    assert type(results) is list
    assert len(results) >0
    # assert len(results)   == 100, "Length was too short, expecting 100 elements . . ."
    for item in results:
        assert type(item) is tuple
    # print(type(results[0]))
    id, task, status = results[0]
    assert type(id) is int
    assert type(task) is str
    # assert type(status) is int
    # assert status in [0,1]

def test_get_item():
    print("Testing get_item(id)")
    results = get_items()
    assert len(results)>0
    id, task, status = results[0]
    result = get_item(id)
    assert type(result) is tuple
    id2, task2, status2 = result
    assert id2 == id
    assert task2 == task
    assert status2 == status

    print(result)


if __name__ == "__main__":
    # test_get_items()
    test_get_item()
    print("Done.")