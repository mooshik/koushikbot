from flask import request, Flask

app = Flask(__name__)

@app.route('/jason')
def serve():
    return request.args.get('well')
