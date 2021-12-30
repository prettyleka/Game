from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def returnHTML():
    f = open("/home/user/PycharmProjects/HomeProject/Game/Scores.txt", "r+")
    result=f.read()
    html = open("/home/user/PycharmProjects/HomeProject/Game/app/templates/Score.html", "r+")
    text = html.read().format(SCORE=result)
    if result != "":
        return text
    else:
        return render_template('Error.html')

if __name__ == '__main__':
    app.run()