from flask import Flask, request
from flask_limiter import Limiter
from flask_cors import CORS, cross_origin
from random import randint
import re

app = Flask(__name__)
CORS(app, support_credentials=True)

limiter = Limiter(
    app,
    key_func=lambda: request.headers.get("X-Real-Ip"),
)
url_regex = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def detect(url: str):
    identifier = randint(0, 1)
    if identifier == 0:
        return "False", 200
    else:
        return "True", 200


@app.route("/vampire", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("30 per month")
def vampire():
    url = request.args.get("url")
    if re.match(url_regex, url) is None:
        return "Bad Request", 400
    return "False", 200  # Impossible to photograph vampires


@app.route("/dog", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("30 per month")
def dog():
    url = request.args.get("url")
    if re.match(url_regex, url) is None:
        return "Bad Request", 400
    return detect(url)


@app.route("/cat", methods=["GET"])
@cross_origin(support_credentials=True)
@limiter.limit("30 per month")
def cat():
    url = request.args.get("url")
    if re.match(url_regex, url) is None:
        return "Bad Request", 400
    return detect(url)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
