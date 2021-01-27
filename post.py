from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_message():
    content = request.json
    print(content['id'])
    return "Hello World!"

if __name__ == '__main__':
    app.run()