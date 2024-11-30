from flask import Flask
#### WSGI APPLICATION
app = Flask(__name__)



### Decorator
@app.route('/')
def welcome() :
    return 'Welcome Flask bro'

@app.route('/students')
def students():
    return 'Welcome students'





if __name__=='__main__':
    app.run(debug=True, port=8080)
