from collections import namedtuple
 
from flask import Flask, render_template, redirect, url_for, request
 
app = Flask(__name__)
 
Message = namedtuple('Message', 'number')
messages = []
 
 
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', messages=messages)
 
 
@app.route('/add_number', methods=['POST'])
def add_message():
    x = request.form['calc']
    messages.append(Message(x))
    return redirect(url_for('index'))
 
 
if __name__ == '__main__':
    app.run()