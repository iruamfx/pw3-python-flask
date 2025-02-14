# Importa pacote Flask do modulo flask
from flask import Flask #as app

# Instanciando Flask no app.py
app = Flask(__name__)

# Rota principal do site
@app.route("/")

# Criar função da home
def home():
    return "<h1>Hello Flask!</h1>"

@app.route("/games")
def games():
    return "<h1>Pagina de games</h1>"

if __name__ == "__main__":
    # Roda servidor no localhost, porta 5000; 0.0.0.0 = rede LAN
    app.run(host="localhost", port=5000, debug=True)