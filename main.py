from flask import Flask, render_template, request
from g4f.client import Client

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        text = request.form['textInput']

        global savedText
        savedText = text

        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": savedText}],
        )

        answer = response.choices[0].message.content

    return render_template('index.html', saved_text=savedText, answer=answer)

if "__main__" == (__name__):
    app.run()