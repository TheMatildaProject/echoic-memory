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
    result = youtube.search(request.json['criteria'])

    return jsonify({
        'id': result,
        'video': 'https://youtube.com/watch?v=' + result
    });

def vote():
    if not request.json or not 'video_id' in request.json:
        return jsonify({'error': 'Missing video_id'}), 400

    return jsonify({
        'success': true,
    });

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)