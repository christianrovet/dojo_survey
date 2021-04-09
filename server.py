from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])
def user_result():
    return render_template('result.html', 
    name = request.form['your_name'],
    location = request.form['location'],
    language = request.form['language'],
    comment = request.form['comment'])


if __name__ == "__main__":
    app.run(debug=True)