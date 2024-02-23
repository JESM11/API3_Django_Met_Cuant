from flask import Flask, jsonify, request


app=Flask(__name__)
@app.route("/fibonacci/<n>")
def fibonacci(n) -> list:
    num=int(n)
    fib_sequence = [0, 1]
    for i in range(2, num):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return jsonify(fib_sequence[:num]),200

@app.route("/LCS/<strings>")
def length_of_longest_common_substring(strings) -> int:
    cadena = strings
    separadas = cadena.split("y")
    s1=separadas[0]
    s2=separadas[1]

    # Inicializar la matriz bidimensional

    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Iterar sobre las dos cadenas
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Devolver la longitud de la subsecuencia común más larga
    return jsonify(dp[-1][-1]),200

if __name__=="__main__":
    app.run(debug=True)