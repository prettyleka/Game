from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def returnHTML():
    f = open("Scores.txt", "r+")
    result=f.read()
    html = open("app/templates/Score.html", "r+")
    text = html.read().format(SCORE=result)
    if result != "":
        return text
    else:
        return render_template('app/templates/Error.html')

if __name__ == '__main__':
    app.run()