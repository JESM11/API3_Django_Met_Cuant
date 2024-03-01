from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5500")

@app.route("/fibonacci", methods=['GET', 'OPTIONS'])
def fibonacci(n=None) -> list:
    if request.method == 'OPTIONS':
        # Respondemos a la solicitud OPTIONS con los encabezados CORS adecuados
        response = jsonify()
        response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
        response.headers.add("Access-Control-Allow-Methods", "GET")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response

    try:
        if n is None:
            n = request.args.get('n')

        if n is None:
            return jsonify({"error": "Parameter 'n' is required."}), 400

        num = int(n)
        fib_sequence = [0, 1]
        for i in range(2, num):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return jsonify(fib_sequence[:num]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route("/lcsmain/<string1>/<string2>", methods=['GET', 'OPTIONS'])
def lcsmain(string1, string2) -> int:
    if request.method == 'OPTIONS':
    # Respondemos a la solicitud OPTIONS con los encabezados CORS adecuados
        response = jsonify()
        response.headers.add("Access-Control-Allow-Origin", "http://127.0.0.1:5500")
        response.headers.add("Access-Control-Allow-Methods", "GET")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response

    m = len(string1)
    n = len(string2)
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]

    
    # Devolver la longitud de la subsecuencia común más larga
    return jsonify(lcs(string1, string2, m, n, dp)),200

def lcs(X, Y, m, n, dp):
    """
    Parametros:
        X (str): Primera string.
        Y (str): Segunda string string.
        m, n: length de cada string.
        dp (list): Lista 2D para usar como memoizacion.
        
    Retorna:
        str: la subsequencia mas larga.
    """
    if m == 0 or n == 0:
        return "" # Caso base

    if X[m - 1] == Y[n - 1]: # Si el ultimo caracter de las dos strings es igual
        return lcs(X, Y, m - 1, n - 1, dp) + X[m - 1] # Agregar el caracter a la subsecuencia

    if dp[m - 1][n] > dp[m][n - 1]: 
        return lcs(X, Y, m - 1, n, dp)
        # Si el ultimo caracter de X y Y son diferentes, usando la lista de memoizacion dp, 
        # se verifica si el valor de dp[m - 1][n] es mayor que dp[m][n - 1], si es asi,
        # se llama recursivamente a la funcion lcs con m - 1 y n, y se retorna el valor.
    else:
        return lcs(X, Y, m, n - 1, dp)
        # Si no es asi, se llama lcs con m y n - 1, y se retorna el valor.


if __name__=="__main__":
    app.run(debug=True)