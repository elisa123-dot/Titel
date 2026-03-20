from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Eingabe = request.form.get('Eingabe')
        if int(Eingabe) == 884900:
            return render_template("indexcopy.html", "richtig", richtantwort="Antwort: 884900", deinantwort= "deine Antwort: ", eeingabe= int(Eingabe))
        else :
            return render_template("indexcopy.html", antwort= round(int(Eingabe)*100/884900,2), prozent="%", richtantwort="Antwort: 884900", deinantwort= "deine Antwort: ", eeingabe= int(Eingabe) )     

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

