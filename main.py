from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/fibonacci": {"origins": "http://127.0.0.1:5500"}})

@app.route("/fibonacci", methods=['GET', 'OPTIONS'])
@app.route("/fibonacci/<int:n>", methods=['GET', 'OPTIONS'])
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

@app.route("/LCS/<string1>/<string2>")
def length_of_longest_common_substring(string1, string2) -> int:
    m = len(string1)
    n = len(string2)
    dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]

    
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
        int: Length de la subsequencia mas larga.
    """
    if (m == 0 or n == 0):
        return 0

    # Si el valor ya fue calculado, retornar el valor.
    if (dp[m][n] != -1):
        return dp[m][n]
    
    # Si el ultimo caracter de ambas strings es igual, agregar 1 al resultado y llamar recursivamente con las strings sin el ultimo caracter.
    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m][n]
    
    # Si el ultimo caracter de ambas strings es diferente, retornar el maximo de llamar recursivamente con las strings sin el ultimo caracter de X y Y.
    dp[m][n] = max(lcs(X, Y, m, n - 1, dp), lcs(X, Y, m - 1, n, dp))
    return dp[m][n]



if __name__=="__main__":
    app.run(debug=True)