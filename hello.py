from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/kindle_push', methods=['POST'])
def kindle_push():
    print(request.data)
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)