from flask import Flask, render_template, request
from google_trans_new import google_translator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/textTranslate')
def text_translate():
    return render_template('textTrans.html', result="")


@app.route('/text_result', methods=['POST', 'GET'])
def text_result():
    if request.method == 'POST':
        input_text = []
        input_text.append(request.form['result'])
        print(input_text)
        trans = google_translator()

        text = trans.translate(text=input_text[0], lang_tgt='hi', lang_src='en')
        print(text)
        return render_template("textTrans.html", result=text)


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug = True)
