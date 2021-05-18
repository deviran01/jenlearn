from flask import Flask

app = Flask(__name__)


@app.route('/<person>')
def hello_world(person):
    return f'Hello {person}'


if __name__ == '__main__':
    app.run()
