from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/encrypt_text" method = 'POST'>
                <label>Rotate by:
                    <input id = 'rot' name = "rot" type = "text" value = '0' />
                </label>
                <textarea id='text' name="text">{0}</textarea>
                <input type = "submit" />
            </form>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form.format("")



@app.route("/encrypt_text" , methods = ['POST'])
def encrypt():
    encryption_key = int(request.form["rot"])
    text_to_encrypt = str(request.form["text"])
    encrypted_text = rotate_string(text_to_encrypt, encryption_key)
    return form.format(encrypted_text)

app.run()
