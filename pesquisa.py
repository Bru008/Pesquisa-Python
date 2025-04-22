from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    nome = request.form['nome']
    mensagem = f"Olá, {nome}!"
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
