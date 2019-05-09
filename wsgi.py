from flask import Flask
import json
import os
import socket

application = Flask(__name__)


# noinspection PyBroadException
@application.route("/", methods=["GET"])
def api_get():
    try:
        data = ({
            "test openshift automatico con variante": os.getenv("NAME", "Test"),
            "hostname para test": socket.gethostname()
        })
    except:
        data = ({
            "code": 404,
            "description": "The server has not found anything matching the request URI",
            "reasonPhrase": "Not Found"
        })

    return json.dumps(data)

if __name__ == "__main__":
    application.run(debug=True, port=5002)
