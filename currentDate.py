from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/greeting')
def roll():
    now_date = datetime.now()
    return str(now_date)


if __name__ == '__main__':
    app.run(debug=True)
