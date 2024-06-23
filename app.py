import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')
    # Definiere eine Liste gültiger Eingaben
    # valid_inputs = ["1 und 2", "2 und 1", "1,2", "2,1", "2&1", "1&2"]
    valid_inputs = ["1 und 2", "2 und 1", "1,2", "2,1", "2&1", "1&2", "1 2", "12", "1/2"]
 
    # Überprüfe, ob die Eingabe in der Liste gültiger Eingaben ist
    if name and any(name.lower() == valid.lower() for valid in valid_inputs):
        print('Haste gut gemacht, mein Jung!')
        return render_template('hello.html', name=name)
    else:
        print('Tja Thaddaus, war wohl nix!')
        return redirect(url_for('index'))

# valid_inputs = ["1 und 2", "2 und 1", "1,2", "2,1", "2&1", "1&2", "1 2", "12", "1/2"]

if __name__ == '__main__':
   app.run()
