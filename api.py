import dboperations
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/act_prices")
def act_prices_endpoint():
    crypto  = request.args.get("crypto")
    fiat    = request.args.get("fiat")
    pamount = request.args.get("pamount", type=float)

    if not crypto or not fiat or pamount is None:
        return jsonify(error="Missing/invalid params: crypto, fiat, pamount"), 400

    try:
        result = dboperations.act_dolar(crypto, fiat, pamount)
        return jsonify(
            message="Actualización de precios exitosa",
            crypto=crypto, fiat=fiat, pamount=pamount, result=result
        ), 200
    except Exception as e:
        app.logger.exception("Error in /act_prices")
        return jsonify(error=str(e)), 500

@app.get("/ping")
def ping():
    return "pong", 200


if __name__ == '__main__':
    app.run(debug=True)