<p>Update Task</p>
<form action="/update_task" method="POST">
    <input type="text" size="100" maxlength="100" name="_id" value="{{str(row['_id'])}}" hidden/>
    <input type="text" size="100" maxlength="100" name="updated_task" value="{{row['text']}}"/>
    <hr/>
    <input type="submit" name="update_button" value="Update"/>
    <a href="/">Cancel</a>
</form>