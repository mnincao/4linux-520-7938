import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
    return "ola"
    
@app.route("/saudacao")
def saudar():
      return 'Ola'