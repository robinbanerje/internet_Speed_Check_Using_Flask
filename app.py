from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home page</h1>"

@app.route('/welcome')
def welcome():
    return "<button>Welcome to flask</button>"

@app.route('/index')
def index():
    return render_template('index.html')

## Variable rule
@app.route('/success/<int:score>')
def success(score):
    return "The student has passed successfully with score: " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The student has failed due to score: " + str(score)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        avg_marks = (maths + science + history)/3

        return render_template('form.html', score = avg_marks)

if __name__=='__main__':
    app.run(debug=True)
