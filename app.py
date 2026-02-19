from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Meine erste Flask-Seite</title>
            </head>
            <body>
                <h1>Willkommen!</h1>
                <p>Das ist meine erste Webseite, serviert von Flask.</p>
            </body>
        </html>
    '''