#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_python=button_python,button_html=button_html,button_db=button_db,button_discord=button_discord)
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.get.form('email')
    text = request.get.form('text')
    return render_template('index.html', text=text,email=email)

if __name__ == "__main__":
    app.run(debug=True)