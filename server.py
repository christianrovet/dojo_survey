from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
app = Flask (__name__)
app.secret_key = "hello!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['post'])
def user_result():
    is_valid = True
    if len(request.form['your_name']) < 1:
        is_valid = False
        flash("Please enter your name")
    if len(request.form['comment']) < 2:
        is_valid = False
        flash("Please enter a comment")
    
    if not is_valid:
        return redirect('/')
    else:
        query = 'INSERT INTO dojos(name,location,language,comment,created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW());'
        data = {
        'name': request.form['your_name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
        }
        connectToMySQL('dojo_survey_schema').query_db(query,data)
        return redirect('/results')

@app.route('/results')
def results():
    query = 'SELECT * FROM dojos'
    users = connectToMySQL('dojo_survey_schema').query_db(query)
    return render_template('results.html', users=users)


if __name__ == "__main__":
    app.run(debug=True)