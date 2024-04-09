from flask import Flask

app = Flask(__name__)

API_KEY = "12345abcde67890fghij"
SECRET_PASSWORD = "verySecretPassword123"

@app.route('/')
def index():
    return "Welcome to the secret Flask app!"

if __name__ == "__main__":
    app.run(debug=True)
