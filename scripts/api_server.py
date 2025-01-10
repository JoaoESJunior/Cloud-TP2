# Código inicial do servidor API
from flask import Flask

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    return {"message": "API funcionando!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
