import json

from flask import request, Flask

app = Flask(__name__)

token = 'EAAZAN5XZBKMSUBAL0QZCjHyhl3OqAGwcoE4kZAQiGowvjQWYk5ROIcsD2mhnBgfvb0YNoPxaOr9C4AOhuPGV9zEy3ZCpekxkPW5jcYZAySKfMLDbQqlQrT3t6roRfz9l2cBFfmyvLM9naO2xOfZBNruVuWoTZCvlyZBwZBa6BmkDOYHwZDZD'

@app.route('/receive', methods=['GET'])
def serve():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'koushik':
        return request.args.get('hub.challenge')
    return 'fuck_you'


@app.route('/receive', methods=['POST'])
def receive():
    print request.data
    data = json.loads(request.data)

    for entry in data['entry']:
        for message in entry['messaging']:
            print message['sender']['id']
            print message['message']['text']

    return 'success'
