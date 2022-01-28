from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def returnHTML():
    f = open("Scores.txt", "r+")
    result=f.read()
    if result != "":
        return render_template('Score.html', SCORE=result)
    else:
        return render_template('Error.html')
