import dboperations
from flask import Flask, request

app = Flask(__name__)

@app.route('/act_prices', methods=['GET'])
def act_prices_endpoint():
    # Get the pamount parameter from the URL
    pamount = request.args.get('pamount')

    # Call the act_prices function
    result = dboperations.act_dolar(pamount)
    return str(result), 200

if __name__ == '__main__':
    app.run(debug=True)