from flask import Flask
from flask_cors import cross_origin
import os

app = Flask(__name__)


@app.route("/")
@cross_origin()
def main():
    return "Welcome to Code Paradox"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', use_reloader=False, port=port)
