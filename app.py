from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "This is the index page"

@app.get("/dd")
def g():
    return "dd"

if(__name__=='__main__'):
    app.run(port = 3000)
