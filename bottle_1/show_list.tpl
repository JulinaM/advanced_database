<p>Todo List</p>
<table border="1">
% for row in rows:
    <tr>
    %for item in row[1:]:
        <td> {{item}} </td>
    %end
        <td>
            <a href="/delete_item/{{row[0]}}">DELETE </a>

        </td>
    </tr>
%end
</table>
<a href="/new_item">New Item ... </a>
<hr/>
<a href="/delete_item/14">We don't like #14 </a>

