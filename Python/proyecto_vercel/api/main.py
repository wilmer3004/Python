from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # código de tu función
        return "HELLO from vercel use flask"
    except Exception as e:
        # registra el error o imprímelo para depuración
        print(str(e))
        return "Error interno del servidor", 500

@app.route("/about")
def about():
    # código de tu función
    return "about"
