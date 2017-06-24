from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run():
    return jsonify({'message': 'It works!'});

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)