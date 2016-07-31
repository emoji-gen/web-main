from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.j2')


if __name__ == '__main__':
    app.run(debug=True)
