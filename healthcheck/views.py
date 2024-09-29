from healthcheck import app

from datetime import datetime

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    response = {
        "status": "OK",
        "current_date": datetime.now().isoformat()
    }
    return response, 200
