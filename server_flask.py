from flask import Flask

app = Flask(__name__)

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bonjour/<name>")
def hello_fael(name):
    return "hey "+name+" cest clairement plus ismple"
  
if __name__ == "__main__":
    app.run()
