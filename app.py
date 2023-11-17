from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def verification():
    data = request.args
    print(data)
    if data.get("hub.mode") == "subscribe" and data.get("hub.verify_token") == "test":
        return data.get("hub.challenge"), 200

@app.route('/webhook', methods=['POST'])
def message():
    # Parse the request body from the POST
    body = request.json

    # Check the Incoming webhook message
    print(json.dumps(body, indent=2))

    # info on WhatsApp text message payload: https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples#text-messages
    test = """    if 'object' in body:
        if (
            'entry' in body and
            body['entry'][0]['changes'] and
            body['entry'][0]['changes'][0] and
            body['entry'][0]['changes'][0]['value']['messages'] and
            body['entry'][0]['changes'][0]['value']['messages'][0]
        ):
            phone_number_id = body['entry'][0]['changes'][0]['value']['metadata']['phone_number_id']
            from_number = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
            msg_body = body['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

            # Assuming 'token' is defined elsewhere in your code
            # Example: token = 'your_access_token'

            # You need to install the 'requests' library to make HTTP requests
            # Install it using: pip install requests
            import requests

            url = f"https://graph.facebook.com/v12.0/{phone_number_id}/messages?access_token={token}"
            data = {
                "messaging_product": "whatsapp",
                "to": from_number,
                "text": {"body": f"Ack: {msg_body}"}
            }
            headers = {"Content-Type": "application/json"}

            # Send POST request using the requests library
            response = requests.post(url, json=data, headers=headers)
    """
    return jsonify({"status": "success"}), 200 if 'object' in body else 404


@app.route('/health-check', methods=['GET'])
def health_check():
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, port=7000)
