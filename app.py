from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jane = request.form.get('jane') 
        if jane == "Nein":
            return render_template("indexxcopy.html", Frage= "Wie hoch ist der Mount Everest (in cm)?")
            Eingabe=request.form.get('eingabe')
            if int(Eingabe) == 884900:
                return render_template("indexcopy.html", "richtig", richtantwort="Antwort:",o=884900 ,deinantwort= "deine Antwort: ", eeingabe= int(Eingabe))
            else :
                return render_template("indexcopy.html", antwort= round(int(Eingabe)*100/884900,2), prozent="%", richtantwort="Antwort: 884900", o=8840900 ,deinantwort= "deine Antwort: ", eeingabe= int(Eingabe) ) 
        else :
            Eingabee=request.form.get('Eingabee')
            return render_template("indexx.html", Frage= Eingabee )
            Antwort=request.form.get('Antwort')
            if int(Eingabe) == Antwort:
                return render_template("indexcopy.html", "richtig", richtantwort="Antwort:", deinantwort= "deine Antwort: ", o=Antwort , eeingabe= int(Eingabe))
            else :
                return render_template("indexcopy.html", antwort= round(int(Eingabe)*100/884900,2), prozent="%", richtantwort="Antwort: ",o=Antwort ,deinantwort= "deine Antwort: ", eeingabe= int(Eingabe) ) 



    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

     

