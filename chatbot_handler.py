from flask import request, Flask

app = Flask(__name__)

@app.route('/jason')
def serve():
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.verify_token') == 'koushik':
        return request.args.get('hub.challenge')
    return 'fuck_you'
