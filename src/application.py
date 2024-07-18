from flask import Flask

application= Flask(__name__)
app=application
@app.route('/')
def index():
    return "Welcome to home page"



if __name__=="__main__":
    app.run(debug=True)