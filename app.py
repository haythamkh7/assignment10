import mysql

from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify
from utilities.db.db_manager import DBManager

app = Flask(__name__)
app.secret_key = '123ab'
if __name__ == '__main__':
    app.run()

from pages.assiggnment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/')
def hello_home():
    return render_template('Aboutmyself.html')

@app.route('/ContactListSite')
def ContactListSite():
    return render_template('ContactListSite.html')

@app.route('/Contactus')
def Contactus():
    return render_template('Contactus.html')

@app.route('/Edection')
def Edection():
    return render_template('Edection.html')

@app.route('/EXPERIENCE')
def EXPERIENCE():
    return render_template('EXPERIENCE.html')

@app.route('/HighschoolGraduation')
def HighschoolGraduation():
    return render_template('HighschoolGraduation.html')

@app.route('/RelevanteCorse')
def RelevanteCorse():
    return render_template('RelevanteCorse.html')

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html',title='',user={'firstname':"haytham",'lastname':"khmaisi"}
                           ,skills=('JAVA','Python','HTML','Database Management','Management Information Systems','Git/HitHub'))

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    users = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
              "avatar": "https://reqres.in/img/faces/7-image.jpg"},
             {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
              "avatar": "https://reqres.in/img/faces/8-image.jpg"},
             {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
              "avatar": "https://reqres.in/img/faces/9-image.jpg"},
             {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
              "avatar": "https://reqres.in/img/faces/10-image.jpg"},
             {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
              "avatar": "https://reqres.in/img/faces/11-image.jpg"},
             {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
              "avatar": "https://reqres.in/img/faces/12-image.jpg"}]
    username = ''
    if request.method == 'GET':
        if 'search' in request.args:
         searchName = request.args['search']
         if searchName == '':
             return render_template('Assignment9.html', users=users)
         else:
          return render_template('Assignment9.html', username=searchName, users=users)

    if request.method == 'POST':
        user= request.form['username']
        session['logged_in'] = True
        session['username'] = user
        return render_template('Assignment9.html')
    return render_template('Assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    session['username'] = ' '
    return render_template('Assignment9.html')

@app.route('/assignment11/users')
def get_users():
    if request.method == "GET":
        query = "select * from users"
        db_manager = DBManager()
        query_result = db_manager.fetch(query=query)
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                'data': []
            })
        else:
            data = []
            for user in query_result:
                data.append({
                    'id:': user.id,
                    'first name:': user.first_name,
                    'last name:': user.list_name,
                    'email:': user.email,
                    'success': 'True'
                })
            return jsonify(data)


@app.route('/assignment11/users/selected/', defaults={'SOME_ID': 10})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def get_my_users(SOME_ID):
    if request.method == "GET":
        query = "select * from users WHERE id='%s'" % (SOME_ID)
        db_manager = DBManager()
        query_result = db_manager.fetch(query=query)
        if len(query_result) == 0:
            return jsonify({
                'success': 'False',
                'data': []
            })
        else:
            user = query_result[0]
            return jsonify({
                'id:': user.id,
                'first name:': user.first_name,
                'last name:': user.list_name,
                'email:': user.email,
                'success': 'True'
            })

