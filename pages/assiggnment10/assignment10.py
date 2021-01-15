import mysql.connector
from flask import Blueprint
from flask import render_template, redirect, request

# about blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static',static_url_path='/assignment10', template_folder='templates')


# Routes

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='1234',
                                         database='flask_haytham')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)  # Query operations

    if query_type == 'commit':
        # use for   add update
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_resulte = cursor.fetchall()
        return_value = query_resulte

    connection.close()
    cursor.close()
    return return_value

@assignment10.route('/insert', methods=['GET','POST'])
def fu_assignment10():
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "INSERT INTO users(id,first_name,list_name ,email) values ('%s','%s','%s','%s') " % (id,first_name, last_name, email)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'Somthing went Wrong'




@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        id = request.args['id']
        query = "DELETE FROM  users WHERE  id ='%s';" % id
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'Somthing went Wrong'


@assignment10.route('/assignment10')
def allusers():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)

@assignment10.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        query = "UPDATE users set first_name=('%s') WHERE id=(%s)" % (first_name, id)
        query1 = "UPDATE users set list_name=('%s') WHERE id=(%s)" % (last_name, id)
        query2 = "UPDATE users set email=('%s') WHERE id=(%s)" % (email, id)
        interact_db(query=query, query_type='commit')
        interact_db(query=query1, query_type='commit')
        interact_db(query=query2, query_type='commit')
        return redirect('/assignment10')
    return 'Something wen wrong'

