from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return 'You clicked on Home!'

@app.route('/okay')
def okay():
    return 'You clicked on Okay!'

if __name__ == '__main__':
    app.run(debug=True)
