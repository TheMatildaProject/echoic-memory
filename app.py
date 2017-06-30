from flask import Flask, request, jsonify
from app.clients.youtube_client import YoutubeClient

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run():
    return jsonify({'message': 'It works!'});

@app.route('/search', methods=['POST'])
def search():
    if not request.json or not 'criteria' in request.json:
        return jsonify({'error': 'Missing search criteria'}), 400

    youtube = YoutubeClient()
    youtube.search()

    return jsonify({'message': 'Searching!'});

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)