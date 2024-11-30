from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome Flask'

@app.route('/success/<int:score>')
def success(score):
    return 'The person passed and marks are ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person failed and marks are ' + str(score)

@app.route('/result/<int:score>')
def result(score):  # Fixed parameter name to match route variable
    # Determine the result based on the score
    if score < 50:
        return redirect(url_for('fail', score=score))  # Redirect to 'fail' route
    else:
        return redirect(url_for('success', score=score))  # Redirect to 'success' route

if __name__ == '__main__':
    app.run(debug=True)
