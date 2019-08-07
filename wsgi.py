from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d.%m.%Y %H:%M:%S")
    return "Hello World! " + timestampStr

if __name__ == "__main__":
    application.run()
