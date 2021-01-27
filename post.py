from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('https://requesthandlerbatuhan.herokuapp.com/', methods=['GET', 'POST'])
def add_message():
    content = request.json
    print(content['id'])

if __name__ == '__main__':
    app.run()