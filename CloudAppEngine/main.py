from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# gcloud app deploy
# gcloud app logs tail -s default
# gcloud app browse