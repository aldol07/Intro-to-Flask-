from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome() :
     return 'Welcome Flask'






if __name__ == "__main__":
    app.run()
# msg = "Welcome Flask"
# print(msg)
# print("Please learn it completely")

