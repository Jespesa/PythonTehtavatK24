from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


#testaa onko alkuluku laittamalla urliin /alkuluku/numero
@app.route('/alkuluku/<int:num>', methods=['GET'])
def check_prime(num):
    if is_prime(num):
        response = {"Number": num, "isPrime": True}
    else:
        response = {"Number": num, "isPrime": False}
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
