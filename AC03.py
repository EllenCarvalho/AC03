import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def numeros_primos():
    primos = []
    contagem = 0
    i = 0
    numero = 0
    saida = 'Primos: '

    while len(primos) < 100:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                contagem += 1
        if contagem == 1:
             primos.append(numero)
        contagem = 0
        numero += 1

    for a in primos:
        i += 1
        a = str(a)
        saida += a
        if i < len(primos):
            saida += ', '
    saida += '.'
    return saida

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port=port)
