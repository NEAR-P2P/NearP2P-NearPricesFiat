import dboperations
from flask import Flask, request

app = Flask(__name__)

@app.route('/act_prices', methods=['GET'])
def act_prices_endpoint():
    # Get the pamount parameter from the URL
    crypto = request.args.get('crypto')
    fiat = request.args.get('fiat')
    pamount = request.args.get('pamount')

    # Call the act_prices function
    result = dboperations.act_dolar(crypto, fiat, pamount)

    # Create a message
    message = f"Actualización de precios exitosa"

    return message, 200

@app.get("/ping")
def ping():
    return "pong", 200


if __name__ == '__main__':
    app.run(debug=True)