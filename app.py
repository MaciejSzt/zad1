from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict')
def predict():
    x = request.args.get('x', default=0, type=float)
    y = request.args.get('y', default=0, type=float)
    suma = x + y
    prediction = 1 if suma > 5.8 else 0
    return jsonify({
        'features': {'x': x, 'y': y},
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')
