# package includes functions that provide day and time info
from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/time')
def example1():
    # use the datetime python module to obtain the current time
    # and store it in variable "time"
    
    time = datetime.datetime.now()

    response = """<!DOCTYPE html>
                  <html>
                      <p>
                        Current Date and Time: {}
                      </p>
                      <a href="/time">Refresh</a>
                  </html>
                  """

    return response.format(time)


if __name__ == "__main__":
    app.run(host='127.0.0.1')
