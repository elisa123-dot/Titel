from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Eingabe = request.form.get('Eingabe')
<<<<<<< HEAD
        {% if int(Eingabe) == 884900 %}
            <p>richtig</p>
        {% else %}
            <p>return "falsch"</p>
        {% endif %}        
=======
        if int(Eingabe) == 884900:
            return render_template("indexcopy.html", "richtig" )
        else :
            return render_template("indexcopy.html", antwort= round(int(Eingabe)*100/884900,2), prozent="%" )    
>>>>>>> ca62d7bbe6ccce7be555f0082087bb5919f04edf

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

