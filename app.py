from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_function():
    return render_template('index.html')
@app.route('/home')
def my_function():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

