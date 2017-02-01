from flask import request, Flask

app = Flask(__name__)

token = 'EAAZAN5XZBKMSUBABWAvzebHZB3myopwucptBEaKmBgaLdam9aFpC2d4rb7QiRiI3wY7Hr8WjLYECPc4qXRATodacvOxS1ZB7g4XRq0SNbVhoZB71l5phRZAJ4v2eOR9GxhxjBDfBZA4OtKOpCikbSPaLLqsOCazkaoPmZAHZAutyFKAZDZD'

@app.route('/receive', methods=['GET'])
def serve():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'koushik':
        return request.args.get('hub.challenge')
    return 'fuck_you'


@app.route('/receive', methods=['POST'])
def receive():
    print request.body.__dict__
