from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Eingabe = request.form.get('Eingabe')
        {% if int(Eingabe) == 884900 %}
            <p>richtig</p>
        {% else %}
            <p>return "falsch"</p>
        {% endif %}        

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

