from flask import Flask, request

app = Flask(__name__)


@app.route('/verification', methods=['GET'])
def verification():
    data = request.args
    if data.get("hub.mode") == "subscribe" and data.get("hub.verify_token") == "test":
        return data.get("hub.challenge"), 200


@app.route('/health-check', methods=['GET'])
def health_check():
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, port=7000)
