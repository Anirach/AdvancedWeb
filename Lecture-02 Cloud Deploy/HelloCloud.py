from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello  Anirach Happy New Year 2021-2050"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=80)