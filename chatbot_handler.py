import json

from random import random
import requests
from flask import request, Flask

app = Flask(__name__)

token = 'EAAZAN5XZBKMSUBAL0QZCjHyhl3OqAGwcoE4kZAQiGowvjQWYk5ROIcsD2mhnBgfvb0YNoPxaOr9C4AOhuPGV9zEy3ZCpekxkPW5jcYZAySKfMLDbQqlQrT3t6roRfz9l2cBFfmyvLM9naO2xOfZBNruVuWoTZCvlyZBwZBa6BmkDOYHwZDZD'  # noqa


@app.route('/receive', methods=['GET'])
def serve():
    if (
        request.args.get('hub.mode') == 'subscribe' and
        request.args.get('hub.verify_token') == 'koushik'
    ):
        return request.args.get('hub.challenge')
    return 'fuck_you'


koush_resps = [
    'sleep is boring -- {inbound_msg} is better',
    '{inbound_msg} this',
    'whips out {inbound_msg}',
    'YAAAAS {inbound_msg} YAAAAAAS',
    'Hello!!!',
    '{inbound_msg} this: whips out financial crisis of 2008',
    'naaaaaaaas',
    'wooow TFTI TO {inbound_msg}',
    'uguuu'
]


@app.route('/receive', methods=['POST'])
def receive():
    print(request.data)
    data = json.loads(request.data)

    try:
        for entry in data['entry']:
            for message in entry['messaging']:
                sender = message['sender']['id']
                content = message['message']['text']
                koush_resp = koush_resps[int(random() * len(koush_resps))].format(inbound_msg=content)  # noqa

                resp_msg = {
                    'recipient': {
                        'id': sender,
                    },
                    'message': {
                        'text': koush_resp,
                    },
                }

                response = requests.post(
                    'https://graph.facebook.com/v2.6/me/messages',
                    params={'access_token': token},
                    json=resp_msg,
                )
                print('Sent requests %s' % json.dumps(resp_msg))
                print('Received response %s' % response.text)
    except Exception as e:
        print(e)
        return 'not handled'

    return 'success'
